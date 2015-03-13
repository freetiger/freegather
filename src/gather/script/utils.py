# -*- coding: utf-8 -*-
'''
Created on 2015年1月12日

@author: heyuxing
'''
import urllib2, cookielib, urllib
import time
import traceback

class HTTPRefererProcessor(urllib2.BaseHandler):
    def __init__(self):
        self.referer = None
    
    def http_request(self, request):
        if ((self.referer is not None) and
            not request.has_header("Referer")):
            request.add_unredirected_header("Referer", self.referer)
        return request

    def http_response(self, request, response):
        self.referer = response.geturl()
        return response
        
    https_request = http_request
    https_response = http_response

    

class ErrorHandler(urllib2.HTTPDefaultErrorHandler):  
    def http_error_default(self, req, fp, code, msg, headers):  
        result = urllib2.HTTPError(req.get_full_url(), code, msg, headers, fp)  
        result.status = code  
        return result
    
'''
移除html标签，特别的：br标签替换成一个空格
'''
def remove_tag(page_src,omit_tag):
    chunk_list = []
    tag_head = "<"+omit_tag
    b_pos = page_src.find(tag_head)
    e_pos = 0
    while b_pos>=0 and e_pos>=0:
        if omit_tag.startswith("br"):
            chunk_list.append(page_src[e_pos:b_pos]+" ")
        else:
            chunk_list.append(page_src[e_pos:b_pos])
        e_pos = page_src.find(">",b_pos)+1
        b_pos = page_src.find(tag_head,e_pos)
    if b_pos == -1 and e_pos >=0:
        chunk_list.append(page_src[e_pos:])
    return ''.join(chunk_list)

'''
URL特殊字符转义
'''            
def urlzhuanyi(in_url):
    in_url = in_url.replace("&amp;","&")    
    return in_url



'''
获得url请求数据的结果htmlsrc
url：请求链接
post_datas：post数据
url前缀做判断：如果是文件则读取文件内容返回，如果是文本内容则直接返回该内容，如果是url则返回该url应答页面的内容。
'''
def getResponse(url, post_datas={}, sleep_time=0, proxies={}, headers={}, urllib2=None):
    resp = ""
    if url is None or len(url)==0:
        return resp
    url = urlzhuanyi(url)
    import random
    sleep_time = random.uniform(2,5)
    if sleep_time>0:
        time.sleep(sleep_time)
    if urllib2 is None:
        urllib2 = init_urllib2()
    
    if headers==None or len(headers)==0:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-cn,zh;q=0.5",
            "Accept-Charset":"gb2312,utf-8;q=0.7,*;q=0.7",
            "Connection": "Keep-Alive",
            "Cache-Control": "no-cache",
            #"Cookie":"skin=noskin; path=/; domain=.amazon.com; expires=Wed, 25-Mar-2009 08:38:55 GMT\r\nsession-id-time=1238569200l; path=/; domain=.amazon.com; expires=Wed Apr 01 07:00:00 2009 GMT\r\nsession-id=175-6181358-2561013; path=/; domain=.amazon.com; expires=Wed Apr 01 07:00:00 2009 GMT"
        }
    req=urllib2.Request(url,headers=headers) #伪造request的header头，有些网站不支持，会拒绝请求;有些网站必须伪造header头才能访问
    try:
        if post_datas:
            url_data = urllib.urlencode(post_datas)
            resp = urllib2.urlopen(req, url_data)
            print "request: "+str(url)+" , post_datas="+str(post_datas)
        else:
            resp = urllib2.urlopen(req)
            print "request: "+str(url)
    except:
        print "ERROR: request time out. url="+url
        print traceback.print_exc()

    return resp

'''
获得url请求数据的结果htmlsrc
url：请求链接
post_datas：post数据
url前缀做判断：如果是文件则读取文件内容返回，如果是文本内容则直接返回该内容，如果是url则返回该url应答页面的内容。
'''
def getUrlContent(url, post_datas={}, sleep_time=0, proxies={}, headers={}, urllib2=None):
    htmlsrc = ""
    try:
        resp = getResponse(url, post_datas, sleep_time, proxies, headers, urllib2)
        if resp:
            htmlsrc =resp.read()                
            code = resp.getcode()
            if code==200:
                response_headers = resp.headers.dict
                if response_headers.get("content-encoding")=="gzip":
                    htmlsrc = gunzip(htmlsrc)
                elif response_headers.get("content-encoding") == "deflate":
                    htmlsrc = deflate(htmlsrc)
            else:
                print "ERROR: code="+str(code)+" url="+url
    except:
        print "ERROR: request time out. url="+url,
        print traceback.print_exc()
        htmlsrc = ""

    return htmlsrc

'''
获得url请求数据的结果htmlsrc
url：请求链接
post_datas：post数据
url前缀做判断：如果是文件则读取文件内容返回，如果是文本内容则直接返回该内容，如果是url则返回该url应答页面的内容。
'''
def getContentType(url, post_datas={}, sleep_time=0, proxies={}, headers={}, urllib2=None):
    content_type = ""
    try:
        resp = getResponse(url, post_datas, sleep_time, proxies, headers, urllib2)
        if resp:
            code = resp.getcode()
            if code==200:
                response_headers = resp.headers.dict
                content_type = response_headers["content-type"]
            else:
                print "ERROR: code="+str(code)+" url="+url
    except:
        print "ERROR: request time out. url="+url,
        print traceback.print_exc()
        content_type = ""

    return content_type

def init_urllib2(proxies={}):
    cj = cookielib.CookieJar()
    if len(proxies)>0:
        proxy_support = urllib2.ProxyHandler(proxies)  
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), HTTPRefererProcessor(), proxy_support, urllib2.HTTPHandler)
    else:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), HTTPRefererProcessor(), )
    urllib2.install_opener(opener)
    return urllib2

def gunzip(data):
    import gzip
    import StringIO
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data

# zlib only provides the zlib compress format, not the deflate format;
def deflate(data):
    import zlib
    import StringIO
    data = StringIO.StringIO( data )
    try:               # so on top of all there's this workaround:
        gz = zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        gz = zlib.decompress(data)
    data = gz.read()
    gz.close()
    return data


def download(download_url, store_file, mode, post_datas={}, sleep_time=0, proxies={}, headers={}, urllib2=None):
    page_src = getUrlContent(download_url, post_datas, sleep_time, proxies, headers, urllib2)
    with open(store_file, mode) as out:
        out.write(page_src)
    return store_file



if __name__ == "__main__":   
    pass
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
    }
    headers=None
    htmlsrc = getUrlContent(url="http://www.dabaoku.com/jiaocheng/wangye/html/2013061218177.shtml", headers=headers )
    print htmlsrc
    
