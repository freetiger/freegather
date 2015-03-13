# -*- coding: utf-8 -*-
'''
Created on 2015年1月12日

@author: heyuxing
'''
import datetime
from gather import utils, dbutils
import re
import os
import arrow
from MySQLdb.constants.FIELD_TYPE import NULL

#抓取停止（抓取请求被禁止）
is_end = False

'''
http://weixin.sogou.com 搜索的结果页的页数，并不准确，需要逼近最后一页确定总页数
'''
def get_page_total(weixin_info_id, openid):
    page_total = 1
    page_current = 1
    totalPages_retrieve_str = re.compile(r'"totalPages":(\d*)')
    page_retrieve_str = re.compile(r'"page":(\d*)')
    while True:
        page_src = utils.getSogouContent("http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid="+openid+"&page="+str(page_current), sleep_time=1)
        if page_src is None:
            return 0
        totalPages = totalPages_retrieve_str.findall(page_src)
        page = page_retrieve_str.findall(page_src)
        if len(totalPages)==0 or len(page)==0:
            print "ERROR: get_page_total error!"
            print page_src
            return 0
        else:
            page_total = int(totalPages[0])
            page_current = int(page[0])
        if(page_current>=page_total):
            break
        else:
            page_current = page_total
    print "sogou page_total(10 results per page)="+str(page_total)
    return page_total     

'''
获得搜狗上微信账号openid的所有文章列表页
'''
def get_article_list_urls(openid, page_total=1):
    base_url = "http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid="+openid+"&page="
    article_list_urls = []
    for index in range(page_total):
        article_list_urls.append(base_url+str(index+1))
    return article_list_urls

'''
扫描搜狗上微信账号的文章列表页，获得文章标题title和文章链接url和发布时间
'''
def scan_article_list(weixin_info_id, openid, look_back=True):
    article_infos = []
    page_total = 1
    page_current = 1
    totalPages_retrieve_str = re.compile(r'"totalPages":(\d*)')
    page_retrieve_str = re.compile(r'"page":(\d*)')
    publish_date_regular_str = re.compile(r'<date><!\[CDATA\[([^]]*)')
    title_url_regular_str = re.compile(r'<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)' )
    #
    db_max_publish_date=None
    if look_back:
        db_max_publish_date_object = dbutils.getWeixinArticleMaxPublishDate(weixin_info_id)
        if db_max_publish_date_object is None:
            db_max_publish_date = arrow.get('2000-1-1', 'YYYY-M-D') #那时候还没微信
        else:
            db_max_publish_date = arrow.get(db_max_publish_date_object)
    while True:
        page_url = "http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid="+openid+"&page="+str(page_current)
        page_src = utils.getSogouContent(page_url)
        #获取文章信息（title/url/publish_date）
        if page_src is None:
            print "ERROR: scan_article_list("+page_url+") error! page_src is None"
            return []
        datas = title_url_regular_str.findall(page_src)
        publish_dates = publish_date_regular_str.findall(page_src)
        if len(datas)==len(publish_dates):
            for index in range(len(datas)):
                article_infos.append({"title":datas[index][0], "url":datas[index][1], "publish_date":publish_dates[index], } )
        else:
            #page_src存在特殊字符
            title_list = utils.parse_block_match(page_src, "<title><![CDATA[", "]]><\/title><url><![CDATA[")
            url_list = utils.parse_block_match(page_src, "]]><\/title><url><![CDATA[", "]]><\/url>")
            if len(title_list)==len(url_list) and len(url_list)==len(publish_dates):
                for index in range(len(title_list)):
                    article_infos.append({"title":title_list[index], "url":url_list[index], "publish_date":publish_dates[index], } )
            else:
                print "ERROR: scan_article_list("+page_url+") error! len(datas)="+str(len(datas))+", len(publish_date)="+str(len(publish_dates))
                print page_src
                return []

        #页面上最小的发布日期比数据库最大时，终止文章列表遍历
        if look_back:
            page_min_publish_dates = publish_date_regular_str.findall(page_src)
            if len(page_min_publish_dates)>0:
                page_min_publish_date_str=page_min_publish_dates[-1]
                page_min_publish_date = arrow.get(page_min_publish_date_str, 'YYYY-M-D')
                if page_min_publish_date<db_max_publish_date:
                    return article_infos
        #当前页数等于或大于总页数，终止文章列表遍历
        totalPages = totalPages_retrieve_str.findall(page_src)
        currentPage = page_retrieve_str.findall(page_src)
        if len(totalPages)==0 or len(currentPage)==0:
            #出现禁止页，抓取取消
            print "ERROR: get_page_total error!"
            print page_src
            return []
        else:
            page_total = int(totalPages[0])
            page_current = int(currentPage[0])
        if(page_current>=page_total):
            break
        else:
            page_current = page_current+1
    print "scan_article_list, weixin_info_id="+str(weixin_info_id)+", size="+str(len(article_infos))
    return article_infos

'''
抓取微信weixin_info_id的文章内容，article_urls为文章标题title和链接url
'''
def scan_article_content(article_urls, weixin_info_id, weixin_name, weixin_no, openid, hasThumbnail=False):
    count =0
    for article_url in article_urls:
        title = article_url.get("title")
        url = article_url.get("url")
        publish_date = article_url.get("publish_date")
        content = utils.getWeixinContent(url, sleep_time=1)
        if content is None:
            is_end = True
            return count
        regular_str = re.compile(r'(http://mmbiz.qpic.cn/mmbiz[^"]*)')
        datas = regular_str.findall(content)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content)
        #去除微信二维码
        js_pc_qr_code = soup.find(id="js_pc_qr_code")
        if js_pc_qr_code is not None:
            js_pc_qr_code.replace_with("")
        #去除评论
        js_cmt_more = soup.find(id="js_cmt_more")
        if js_cmt_more is not None:
            js_cmt_more.replace_with("")
        js_cmt_mine = soup.find(id="js_cmt_mine")
        if js_cmt_mine is not None:
            js_cmt_mine.replace_with("")
        #html5图片展示使其适应于html4
        img_list = soup.find_all(attrs={"data-src": True, })
        for img in img_list:
            img["src"]=img["data-src"]
        content = str(soup) 
        weixin_article_id = dbutils.saveWeixinArticle(weixin_info_id, weixin_name, weixin_no, openid, title, url, content, publish_date, "", "")
        count=count+1
        #缩略图
        if hasThumbnail and len(datas)>0:
            for index in range(len(datas)):
                result = utils.download_thumbnail_weixin_image(datas[index].replace("?tp=webp", ""), str(weixin_no)+"/"+str(weixin_article_id)+".jpg", str(weixin_no)+"/"+str(weixin_article_id)+".jpg" )
                if result:
                    dbutils.updateWeixinArticleById(weixin_article_id, thumbnail_url=datas[index])
                    break
    print "Newly added article total="+str(count)
    return count

def gen_thumbnail(thumbnail_url, thumbnail_src_file, thumbnail_tgt_file):
    from weixinarticle.settings import THUMBNAIL_SRC_ROOT, THUMBNAIL_TGT_ROOT, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT
    if not os.path.exists(THUMBNAIL_SRC_ROOT):
        os.makedirs(THUMBNAIL_SRC_ROOT)
    if not os.path.exists(THUMBNAIL_TGT_ROOT):
        os.makedirs(THUMBNAIL_TGT_ROOT)
    infile = THUMBNAIL_SRC_ROOT+thumbnail_src_file
    outfile = THUMBNAIL_TGT_ROOT+thumbnail_tgt_file
    utils.download_weixin_image(thumbnail_url, infile)
    utils.thumbnail(infile, outfile, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT)
    return outfile


'''
过滤掉已抓取过的文章链接
'''
def article_urls_filter(article_urls, weixin_info_id):
    urls = dbutils.getWeixinArticleUrls(weixin_info_id)
    temp_article_urls = []
    #文章列表按照时间正序排列，即搜索结果的倒序；并去重复
    for article_url in article_urls[::-1]:
        if article_url.get("url") not in urls and article_url not in temp_article_urls:
            temp_article_urls.append(article_url)
    return temp_article_urls
    
'''
扫描指定微信公众账号的文章
weixin_info_id：微信信息表WeixinInfo的id
openid：微信公众账号的openid
is_add：是否增量扫描，默认是True
'''
def scan_article(weixin_info_id=None, openid=None, is_add=True, look_back=True):
    if is_end:
        print "is_end="+str(is_end)
        return
    print "scan_article: weixin_info_id="+str(weixin_info_id)+", openid="+str(openid)+", is_add="+str(is_add)
    if weixin_info_id is None and openid is None:
        print "scan_article need params(weixin_info_id or openid)!"
        return
    elif weixin_info_id is not None:
        weixinInfoList = dbutils.getWeixinInfoList(id=weixin_info_id)
    else:
        weixinInfoList = dbutils.getWeixinInfoList(openid=openid)
    for weixinInfo in weixinInfoList:
        weixin_info_id = weixinInfo.id
        weixin_name = weixinInfo.weixin_name
        openid = weixinInfo.openid
        weixin_no = weixinInfo.weixin_no
        article_urls = scan_article_list(weixin_info_id, openid, look_back)
        if is_add:
            article_urls = article_urls_filter(article_urls, weixin_info_id)
        update_num = scan_article_content(article_urls, weixin_info_id, weixin_name, weixin_no, openid, hasThumbnail=True)
        #抓取时间和文章数更新
        dbutils.updateWeixinInfoById(id=weixin_info_id, last_scan_date=str(datetime.datetime.now()), update_num=update_num)
        return ""
    #
    return ""

def gen_weixin_article_reproduced(weixin_info_id=None):
    weixinArticleList = dbutils.getWeixinArticleList(weixin_info_id=weixin_info_id, reproduced_num=NULL, offset=0, limit=10)
    for weixinArticle in weixinArticleList:
        print "gen_weixin_article_reproduced"+str(weixinArticle.weixin_info_id)+":"+weixinArticle.title
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(weixinArticle.content)
        js_content = soup.find(id="js_content")
        print len(js_content.find_all("p")),js_content.find_all("p")[0].get_text(), js_content.find_all("p")
#         js_content_text = js_content.get_text(strip=True)#html页面的看见字符
#         js_content_text_len = len(js_content_text)
#         keyword_1 = js_content_text[js_content_text_len/4:js_content_text_len/4+40]
#         keyword_2 = js_content_text[js_content_text_len/4*2:js_content_text_len/4*2+40]
#         keyword_3 = js_content_text[js_content_text_len/4*3:js_content_text_len/4*3+40]
#         weixinArticleReproducedRecord_list_1 = search_weixin_article(keyword=keyword_1)
#         weixinArticleReproducedRecord_list_2 = search_weixin_article(keyword=keyword_2)
#         weixinArticleReproducedRecord_list_3 = search_weixin_article(keyword=keyword_3)
#         max_len = max(len(weixinArticleReproducedRecord_list_1), len(weixinArticleReproducedRecord_list_2), len(weixinArticleReproducedRecord_list_3))
#         min_len = min(len(weixinArticleReproducedRecord_list_1), len(weixinArticleReproducedRecord_list_2), len(weixinArticleReproducedRecord_list_3))
#         weixinArticleReproducedRecord_list = None
#         keyword = None
#         if min_len<=len(weixinArticleReproducedRecord_list_1)<=max_len:
#             weixinArticleReproducedRecord_list = weixinArticleReproducedRecord_list_1
#             keyword = keyword_1
#         elif min_len<=len(weixinArticleReproducedRecord_list_2)<=max_len:
#             weixinArticleReproducedRecord_list = weixinArticleReproducedRecord_list_2
#             keyword = keyword_2
#         else:
#             weixinArticleReproducedRecord_list = weixinArticleReproducedRecord_list_3
#             keyword = keyword_3
#         #存储weixinArticleReproducedRecord_list
#         weixin_article_reproduced_id = dbutils.saveWeixinArticleReproduced(weixinArticle.weixin_info_id, weixinArticle.id, len(weixinArticleReproducedRecord_list), keyword)
#         for weixinArticleReproducedRecord in weixinArticleReproducedRecord_list:
#             dbutils.saveWeixinArticleReproducedRecord(weixin_article_reproduced_id, weixinArticleReproducedRecord.weixin_name, weixinArticleReproducedRecord.openid, weixinArticleReproducedRecord.title, weixinArticleReproducedRecord.url, weixinArticleReproducedRecord.publish_date)  
    
def search_weixin_article(keyword):
    '''
    文章转载量的统计
    文章被抄袭，title大多会被修改，且title关键词太多，搜索引擎采取的模糊匹配，短词组匹配率高，采用title判断转载量准确率低。；
    大多抄袭文章都不会认真修改，中间段落基本不会被修改，随机截取文章中的稍长句子，到搜索引擎中搜索匹配很高。
    考虑绝大数情况的准确率，一篇文章需要多次截取匹配（暂定三次），开头结尾避免采用。
    
    文章搜素结果页源码有：
    <!--STATUS total 10 time 115 page 2 maxEnd 24 totalItems 24-->
    文章数：totalItems 24
    '''
    print "search_weixin_article start, keyword="+keyword
    import urllib
    weixinArticleReproducedRecord_list = []
    
    #keyword=吹牛说起大学就预测出微博类的产品会火，比特币刚出来几乎还没什么人知道的时候还挖了
    #keyword=%E5%90%B9%E7%89%9B%E8%AF%B4%E8%B5%B7%E5%A4%A7%E5%AD%A6%E5%B0%B1%E9%A2%84%E6%B5%8B%E5%87%BA%E5%BE%AE%E5%8D%9A%E7%B1%BB%E7%9A%84%E4%BA%A7%E5%93%81%E4%BC%9A%E7%81%AB%EF%BC%8C%E6%AF%94%E7%89%B9%E5%B8%81%E5%88%9A%E5%87%BA%E6%9D%A5%E5%87%A0%E4%B9%8E%E8%BF%98%E6%B2%A1%E4%BB%80%E4%B9%88%E4%BA%BA%E7%9F%A5%E9%81%93%E7%9A%84%E6%97%B6%E5%80%99%E8%BF%98%E6%8C%96%E4%BA%86
    keyword_len = len(keyword)
    is_completed = True
    page = 1
    #标红
    page_red_str = re.compile(r'<!--red_end--></em>.{1}<em><!--red_beg-->')
    #发布日期：var date = new Date(time * 1000);
    page_publish_date_str = re.compile(r"vrTimeHandle552write\('([^']*)'")
    while True:
        page_url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&page="+str(page)+"&"+urllib.urlencode({"query":keyword.encode('utf-8')})
        page_src = utils.getSogouContent(page_url, sleep_time=1)
        #预处理，替换单符号间隔</em>,<em>等，“,”只是用来占一个字符位
        page_src, number=page_red_str.subn(",", page_src)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page_src)
        #
        sogou_weixin_name_openid_list = []
        weixin_account_list = soup.find_all("a", id="weixin_account")
        for weixin_account in weixin_account_list:
            sogou_weixin_name_openid_list.append((weixin_account.get("title"), weixin_account.get("i")))
        #
        sogou_article_title_url_list = []
        h4_list = soup.find_all("h4")
        for h4 in h4_list:
            sogou_article_title_url_list.append((h4.a.get_text(), h4.a.get("href")))
        #
        sogou_publish_date_list = []
        publish_date_datas = page_publish_date_str.findall(page_src)
        for publish_date_data in publish_date_datas:
            sogou_publish_date_list.append(str(arrow.get(publish_date_data).date()))
        #
        sogou_summary_list = soup.find_all("p", id=re.compile("sogou_vr_*"))
        for index in range(len(sogou_summary_list)):
            red_item_list = sogou_summary_list[index].find_all("em" )
            for red_item in red_item_list:
                print len(red_item.get_text()),red_item.get_text()
                if len(red_item.get_text())>=keyword_len:
                    print len(red_item.get_text()),red_item.get_text()
                    #匹配到了文章
                    is_completed = False
                    from gather.models import WeixinArticleReproducedRecord
                    weixinArticleReproducedRecord = WeixinArticleReproducedRecord()
                    weixinArticleReproducedRecord.weixin_name = sogou_weixin_name_openid_list[index][0]
                    weixinArticleReproducedRecord.openid = sogou_weixin_name_openid_list[index][1]
                    weixinArticleReproducedRecord.title = sogou_article_title_url_list[index][0]
                    weixinArticleReproducedRecord.url = sogou_article_title_url_list[index][1]
                    weixinArticleReproducedRecord.publish_date = sogou_publish_date_list[index]
                    weixinArticleReproducedRecord_list.append(weixinArticleReproducedRecord)
                    break
                else:
                    is_completed = True
            if is_completed:
                break
        if is_completed:
            break
        else:
            page = page+1
    return weixinArticleReproducedRecord_list
    

'''
搜索keyword相关的微信号，weixin_name、weixin_no、openid
'''
from celery import task
@task(name='search_weixin_info')
def search_weixin_info(keyword, is_all=False):
    print "search_weixin_info start, keyword="+keyword
    import urllib
    weixin_infos = []
    page_url = "http://weixin.sogou.com/weixin?type=1&"+urllib.urlencode({"query":keyword})
    while True:
        page_src = utils.getSogouContent(page_url, sleep_time=1)
        page_src = utils.remove_tag(page_src, "em")
        page_src = utils.remove_tag(page_src, "/em")
        page_src = utils.remove_tag(page_src, "!--red_beg--")
        page_src = utils.remove_tag(page_src, "!--red_end--")
        regular_str = re.compile(r'<h3>([^<]*)</h3>[^<]*<h4>[^<]*<span>微信号：([^<]*)</span>')
        datas = regular_str.findall(page_src)
        #openid
        openid_regular_str = re.compile(r'gotourl\(\'/gzh\?openid=([^\']*)')
        openids = openid_regular_str.findall(page_src)
        if len(datas)==len(openids):
            for index in range(len(datas)):
                weixin_infos.append((datas[index][0], datas[index][1], openids[index]), )
        else:
            print "ERROR: search_weixin_info("+keyword+") error! len(datas)="+str(len(datas))+", len(openids)="+str(len(openids))
            print page_src
            return []
        #
        nextpage_regular_str = re.compile(r'<a id="sogou_next" href="([^"]*)')
        nextpage = nextpage_regular_str.findall(page_src)
        if is_all!=True or len(nextpage)==0:
            break
        else:
            page_url = "http://weixin.sogou.com/weixin"+nextpage[0]
    print weixin_infos
    return weixin_infos

def temp_get_weixin_info(weixin_no):
    weixin_no = weixin_no.strip()
    page_url = "http://w.sugg.sogou.com/sugg/ajaj_json.jsp?key="+weixin_no+"&type=wxpub&ori=yes&pr=web&abtestid=&ipn="
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate,sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"w.sugg.sogou.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",     
    }
    page_src = utils.getSogouContent(page_url, headers=headers)
    page_src = page_src.decode('GBK').encode('utf8')
    regular_str = re.compile(r'\["'+weixin_no+r'",\[([^]]*)')
    datas = regular_str.findall(page_src)
    print "get_weixin_info, datas="+str(datas)
    if datas:
        data_list = datas[0].split(",")
        for data in data_list:
            weixin_name =  data.replace("\"", "")
            weixin_infos = search_weixin_info(weixin_name)
            print weixin_infos
            for weixin_info in weixin_infos:
                if weixin_info[1]==weixin_no:
                    return weixin_info
    return None

def get_xici_proxies():
    proxies=[]
    #国内透明代理IP
    page_src = utils.gatherXici("http://www.xici.net.co/nt/1" )
    regular_str = re.compile(r'<td>(\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b)</td>[^<]*<td>(\d*)')
    datas = regular_str.findall(page_src)
    print page_src
    for data in datas:
        print data
        proxies.append(data[0]+data[1])
    print proxies
    

if __name__ == "__main__":   
    gen_weixin_article_reproduced(weixin_info_id=5)
#     search_weixin_article(keyword="吹牛说起大学就预测出微博类的产品会火，比特币刚出来几乎还没什么人知道的时候还挖了")
    #scan_article(openid="oIWsFt-Atb62Noyz4nKX1nvrmFHQ")
    #print search_weixin_info("晓说", True)
#     article_list_urls = ["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt21qMCAR53L_nCd27iMBnOs&page=7", ]
#     print scan_article_list(article_list_urls)
    #print utils.getUrlContent("http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-dFFZ9mZdL2K9OIZBi9oBg&page=32")
#     import time
#     print time.time()
#     print str(time.time()).replace(".","0")
#     print utils.getUrlContent("http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt9FjqlkRSJGxc-a_1SMFSYo&page=1&t="+str(time.time()).replace(".","0"))
#     get_xici_proxies()
#     print get_weixin_info("dongjian2015")

    
        
        
    