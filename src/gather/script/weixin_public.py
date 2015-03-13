# -*- coding: utf-8 -*-
'''
Created on 2015年1月12日

@author: heyuxing
'''
from gather.job.models import Job, WeixinArticleListScan, WeixinArticle
from gather.script.grabber import Grabber
from gather.script import utils
import re


'''
http://weixin.sogou.com 搜索的结果页的页数，并不准确，需要逼近最后一页确定总页数
'''
def get_page_total(openid):
    page_total = 1
    page_current = 1
    param_retrieve_str = re.compile(r'"totalPages":(\d*),"page":(\d*)')
    while True:
        page_src = utils.getUrlContent("http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid="+openid+"&page="+str(page_current))
        params = param_retrieve_str.findall(page_src)
        print params
        page_total = int(params[0][0])
        page_current = int(params[0][1])
        if(page_current>=page_total):
            break
        else:
            page_current = page_total
        
    return page_total     

def gen_article_list_scan_page(base_url, page_total=1):
    scan_page = "inline:///"
    for index in range(page_total):
        scan_page = scan_page+";"+base_url+str(index+1)
    return scan_page

def scan_article_list(job_id, openid):
    job = Job.objects.get(pk=job_id)
    if job is not None:
        job_name = job.job_name
        get_rules = job.get_rules
        placeholders = {}
        thread_num = 1
        #
        base_url = "http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid="+openid+"&page="
        list_page = gen_article_list_scan_page(base_url, get_page_total(openid))
        get_rules = get_rules.replace("{{list_page}}", list_page)
        Grabber().startscan(job_id=job_id, job_name=job_name, get_rules=get_rules, placeholders=placeholders, thread_num=thread_num)
  
def gen_article_content_scan_urls(job_id):
    article_urls = []
    job = Job.objects.get(pk=job_id)
    if job is not None:
        scanList = job.scan_set.all() 
        for scan in scanList:
            scanResultList = scan.scanresult_set.all() 
            for scanResult in scanResultList:
                temp_scanResult = scanResult.scan_result.split("\t")
                article_urls.append({"title": temp_scanResult[0], "url": temp_scanResult[1]}, )
    return article_urls      
        
def scan_article_content(job_id, weixin_article_list_scan_id):
    weixinArticleListScan = WeixinArticleListScan.objects.get(pk=weixin_article_list_scan_id)
    article_urls = gen_article_content_scan_urls(weixinArticleListScan.job_id)
    weixin_info_id = weixinArticleListScan.weixin_info.id
    #抓取文章页面
    for article_url in article_urls:
        title = article_url.get("title")
        url = article_url.get("url")
        content = utils.getUrlContent(url)
        weixinArticle = WeixinArticle(weixin_info_id=weixin_info_id, title=title, url=url, content=content)
        weixinArticle.save()

if __name__ == "__main__":   
#         base_url = "http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page="
#         list_page = gen_article_list_scan_page(base_url, get_page_total())
#         print "list_page="+list_page
#         print get_page_total()
        
        scan_article_content()
        
        
    