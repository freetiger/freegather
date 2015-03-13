# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: heyuxing
'''

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from gather.script import utils
from django.http import HttpResponse
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import re
from django.db import models

#正在分析的入口网址
gather_site_dict = {}
#

class GatherData(models.Model):
    web_site = models.CharField(max_length=1024, verbose_name='入口网址') #类型再修改
    source = models.TextField(default="", verbose_name='入口网址源代码')
    
    

def show_gather_site(request, gather_site_id):
    '''
    #<span name="selected_1161_span" style="border:1px solid red;background-color:red;">标红选中元素</span>
    #TODO selected_soup中查找所有拥有可见文本的dom节点或有href链接的dom节点。从selected_soup的第一个节点开始查找，后面的节点可能自动补上了完成标记。
    #头尾两节点可能可见文字选取的不全，需要模糊匹配。全文本标红。
    #通过相邻节点的相邻关系，唯一确定在soup中的位置，最后转成用dom结构唯一确定选取的位置，并标红。
    #后续点击调整时，依据tag中的属性值来模糊匹配整个页面中的同类元素，并依次标红。
    #单独设计翻页元素的提取
    '''
    soup = gather_site_dict.get(gather_site_id)
    if soup==None:
        html = "<html><body>竟然出错了.</body></html>" 
    else:
        match_tag_list = []
        selectedContents = request.GET.get('selectedContents', default="")
        if len(selectedContents)>0:
            temp = selectedContents.replace('%','\\')
            selectedContents = temp.decode( 'unicode-escape' )
            match_tag_list.extend(find_tags(soup, selectedContents))
        print match_tag_list
        '''
        写切换程序，在多个值match_tag_list中选择目标值
        改为完全的dom结构匹配，去除text文本部分匹配
        '''
        for match_tag in match_tag_list:
            #NavigableString ok ，再检查Tag
            #需要改为dom结构去确认页面所选元素的位置。应对翻页
            new_tag = soup.new_tag("span" )
            new_tag.attrs={'name': "selected_1161_span", "style":"border:1px solid red;background-color:red;"}
            if type(match_tag) is NavigableString:
                match_tag.wrap(new_tag)
            else:
                for item in match_tag.strings:
                    item.wrap(new_tag)
            
        html = soup.prettify()
    #
    return HttpResponse(html)

def find_tags(soup, selectedContents):
    '''
    通过selectedContents到soup中匹配出合符条件的节点。
    1、先用selectedContents中的第一个节点匹配，如果有多个匹配结果，再用之后的兄弟节点匹配。
    '''
    result_list = []
    need_delete_tag_list = []
    selected_soup = BeautifulSoup(selectedContents)
    selected_contents = selected_soup.body.contents
    if len(selected_contents)>0:
        current_tag = selected_contents[0]
        if type(current_tag) is NavigableString:
            result_list = soup.find_all(text=re.compile(current_tag.strip()))
        else:
            result_list = soup.find_all(name=current_tag.name, attrs=current_tag.attrs)
        for result in result_list:
            if equal_blur_text(result, current_tag):#有空串？？
                result_next_siblings = list(result.next_siblings)
                current_tag_next_siblings = list(current_tag.next_siblings)
                for index in range(len(current_tag_next_siblings)):
                    if not equal_blur_text(result_next_siblings[index], current_tag_next_siblings[index]):
                        need_delete_tag_list.append(result)
                        break
                #补充后面的兄弟节点
                #先不补充兄弟节点，一次标记多个tag不好匹配。用户可以分多次选择标记
                
            else:
                need_delete_tag_list.append(result)
        #移除不匹配的结果
        for need_delete_tag in need_delete_tag_list:
            for result in result_list:
                if id(need_delete_tag)==id(result):
                    result_list.remove(result)
                    break
    return result_list
    
def equal_blur_text(first_tag, second_tag):
    '''
    判断first_tag和second_tag两个标记Tag是否相等.
    模糊比较的地方是：1、first_tag的text包含second_tag的text即可。 2、first_tag的子节点可以比second_tag，但是顺序得一致。
    '''
    #所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
    if type(first_tag) is NavigableString and type(second_tag) is NavigableString:
        if first_tag.find(second_tag.strip())>-1:
            return True
        else:
            return False
    elif type(first_tag) is Tag and type(second_tag) is Tag:
        #检查当前节点是否一致
        if first_tag.name!=second_tag.name or first_tag.attrs!=second_tag.attrs:
            return False
        #检查子节点是否一致
        first_tag_descendants = list(first_tag.descendants)
        first_tag_descendants = filter(lambda tag:(type(tag) is NavigableString and tag.strip()!="") or (type(tag) is not NavigableString),first_tag_descendants)
        second_tag_descendants = list(second_tag.descendants)
        second_tag_descendants = filter(lambda tag:(type(tag) is NavigableString and tag.strip()!="") or (type(tag) is not NavigableString),second_tag_descendants)
        if len(first_tag_descendants)<len(second_tag_descendants):
            return False
        for index in range(len(second_tag_descendants)):
            second_tag_descendant = second_tag_descendants[index]
            first_tag_descendant = first_tag_descendants[index]
            if not equal_blur_text(first_tag_descendant, second_tag_descendant):
                return False
        return True
    else:
        return False

@csrf_exempt
def index(request):
    #TODO 不能添加自己，会死循环，要加判断  http://127.0.0.1:8000/page/
    tgt_website = request.POST.get('tgt_website', default="")
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR']  
    gather_site_id = ip
    #
    htmlsrc = utils.getUrlContent(url=tgt_website, headers=None )
    if htmlsrc.strip()=="":
        htmlsrc = u"<html><body><h1>你输入的网址没找到啊</h1></body></html>"
        soup = BeautifulSoup(htmlsrc)
        gather_site_dict[gather_site_id] = soup
        context = {"tgt_website": tgt_website, "gatherFrame_src": "/page/show_gather_site/"+str(gather_site_id), }
    else:
        soup = BeautifulSoup(htmlsrc)
        base_url = tgt_website
        #有部分网站有防iframe框架设置，如http://www.ablesky.com/lwschool，这类少数网站再改<input id="isAbleskyDomain" type="hidden" value="false">
        #html页面中一些元素的相对路径改为绝对路径
        relative_to_absolute_path(soup, {"link":"href", "script":"src", "img":"src", }, base_url)
        gather_site_dict[gather_site_id] = soup
        context = {"tgt_website": tgt_website, "gatherFrame_src": "/page/show_gather_site/"+str(gather_site_id), }

    return render(request, 'gather/page/index.html', context)

def relative_to_absolute_path(soup, items, base_url):
    '''
    html页面中一些元素的相对路径改为绝对路径
    soup：BeautifulSoup对象
    items：需要更换相对路径的元素{item_name, item_path_attr} 如：{'a':'href', 'img':'src', 'script':'src', 'link':'href'}
    base_url：绝对路径的url，包含要增加到items元素前的域名
    ps：
    #源码中link写链接为相对路径时，在其前增加base_url的host前缀，编程绝对链接。源码中link写的链接为绝对路径时，其值不变。
    link_set = soup.findAll('link')
    for link in link_set:
        link['href'] = urljoin(base_url, link['href'])
    '''
    from urlparse import urljoin
    for item_name, item_path_attr in items.items():
        item_set = soup.findAll(item_name)
        for item in item_set:
            if item.get(item_path_attr) != None:
                item[item_path_attr] = urljoin(base_url, item[item_path_attr])

@csrf_exempt
def run_job_form(request):
    print request.POST.get('tgt_website')
    context = {}
    return render(request, 'gather/page/run_job_form.html', context)



