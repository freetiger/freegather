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

'''
进度：
1、选中的纯文本可以正确匹配，调整，确认规则
2、选中带标签的元素，去除无关项有问题，需改进
3、“相似”模糊匹配，将采取从叶子节点回溯到根节点的方式，逐渐模糊匹配（即兄弟节点是同类标签且属性一致），还未做实现。
4、依据生成的规则进行抓取还未完成，待处理。
5、发现一个同类功能的开源程序portia，先看看。
'''


#正在分析的入口网址
gather_data_dict = {}
#

class GatherData(models.Model):
    user_id = models.CharField(max_length=32, verbose_name='用户标识') #ip、用户名、sessionid等
    web_site = models.CharField(max_length=1024, verbose_name='入口网址') #类型再修改
    src_soup = models.TextField(default="", verbose_name='入口网址源代码')
    soup = models.TextField(default="", verbose_name='当前源代码')
    selected_contents = models.CharField(max_length=1024, verbose_name='选择的页面内容')
    match_tag_list = [] #调整匹配中的当前可能选中的html标签
    match_tag_index = 0 #调整匹配中的当前可能选中的html标签的位置
    gatherModel = "equal"#equal or similar
#     match_tag_type = 
    selected_rule_list = [] #选中的规则 [[下标,name,attrs],[下标,name,attrs],]
    
def show_gather_site(request, gather_site_id):
    '''
    #<span name="selected_1161_span" style="border:1px solid red;background-color:red;">标红选中元素</span>
    #TODO selected_soup中查找所有拥有可见文本的dom节点或有href链接的dom节点。从selected_soup的第一个节点开始查找，后面的节点可能自动补上了完成标记。
    #头尾两节点可能可见文字选取的不全，需要模糊匹配。全文本标红。
    #通过相邻节点的相邻关系，唯一确定在soup中的位置，最后转成用dom结构唯一确定选取的位置，并标红。
    #后续点击调整时，依据tag中的属性值来模糊匹配整个页面中的同类元素，并依次标红。
    #单独设计翻页元素的提取
    '''
    gatherData = gather_data_dict.get(gather_site_id)
    if gatherData==None:
        html = "<html><body>竟然出错了.</body></html>" 
    else:
        soup = gatherData.soup
        action = request.GET.get('action', default="")
        if action=='selectSrc':
            match_tag_list = []
            #gatherData.soup = BeautifulSoup(gatherData.src_soup.prettify())    #做新的匹配项前，还原源代码
            soup = gatherData.soup
            clearMarkColor(soup)
            selectedContents = request.GET.get('selectedContents', default="")
            if len(selectedContents)>0:
                temp = selectedContents.replace('%','\\')
                selectedContents = temp.decode( 'unicode-escape' )
                match_tag_list.extend(find_tags(soup, selectedContents))
            gatherData.selected_contents = selectedContents
            gatherData.match_tag_list = match_tag_list
            gatherData.match_tag_index=0    #gatherData.match_tag_index默认0，先标红第一个，之后再调整
            if len(gatherData.match_tag_list)>0:
                print gatherData.match_tag_list
                for match_tag in gatherData.match_tag_list:
                    markYellowTag(soup, match_tag)
                match_tag = gatherData.match_tag_list[gatherData.match_tag_index]
                markRedYellowTag(soup, match_tag)
            else:
                print '选中页面元素后，我竟然没匹配到！！！'+str(selectedContents)
            #之前已成功匹配的标红   
#             for selected_rule in gatherData.selected_rule_list:
#                 match_tag=find_match_tag(soup, selected_rule)
#                 if match_tag is not None:
#                     markRedBackgroundTag(match_tag)
        elif action=='adjustSrc':   #下一个
            if len(gatherData.match_tag_list)>1:
                match_tag = gatherData.match_tag_list[gatherData.match_tag_index]
                unmarkRedTag(match_tag)
                gatherData.match_tag_index = (gatherData.match_tag_index+1)%len(gatherData.match_tag_list)
                match_tag = gatherData.match_tag_list[gatherData.match_tag_index]
                markRedYellowTag(soup, match_tag)
            else:
                print '选择页面元素后才能做调整'
        elif action=='selectSimilar':
            #当前这个模糊匹配
            match_tag = gatherData.match_tag_list[gatherData.match_tag_index]
            if type(match_tag) is NavigableString:
                result_list = soup.find_all(name=match_tag.parent.name, attrs=match_tag.parent.attrs)
            else:
                result_list = soup.find_all(name=match_tag.name, attrs=match_tag.attrs)
            markRedYellowTag(soup, result_list)
        elif action=='selectedItem':
            if len(gatherData.match_tag_list)>0:
                #生成抓取的规则，DOM上下文逻辑 selected_rule_list TODO
                match_tag=gatherData.match_tag_list[gatherData.match_tag_index]
                rule = gen_gather_rule(match_tag)
                selectedItemMarkColor(soup, match_tag)
                print "rule="+str(rule)
                gatherData.selected_rule_list.append(rule)
                print "gatherData.selected_rule_list="+str(gatherData.selected_rule_list)
                gatherData.match_tag_list=[]
                gatherData.match_tag_index=0
            else:
                print '选择页面元素后才能确认选择'
        elif action=='submitGather':
            pass
        else:
            pass
            
        html = soup.prettify()
    #
    return HttpResponse(html)

def find_match_tag(soup, rule):
    '''
    根据规则查找页面元素，并返回
    '''
    match_tag = None
    if rule is not None and type(rule)==type([]) and len(rule)>0:
        for rule_item in rule:
            if match_tag is None:#首次进入匹配，匹配body标签
                match_tag=find_tag(soup, rule_item)
            else:
                match_tag=find_tag(match_tag, rule_item)
                if match_tag is None:#匹配失败了
                    break
    return match_tag
            
def find_tag(parent_tag, rule_item):
    '''
    根据父节点和规则元素查找页面元素
    '''
    match_tag = None
    index=rule_item[0]
    if rule_item[1] is None:#是NavigableString，到叶子了
        parent_tag_children=list(parent_tag.children)
        if len(parent_tag_children)>index:
            match_tag=parent_tag_children[index]
        else:#有问题的情况 None
            pass
        print match_tag
    else:
        match_tag_list=parent_tag.find_all(name=rule_item[1], attrs=rule_item[2])
        if len(match_tag_list)>index:#index==0时可以做优化
            match_tag=match_tag_list[index]
        else:#有问题的情况 None
            pass
        print str(match_tag.name)+str(match_tag.attrs)
    return match_tag
    
def gen_gather_rule(match_tag):
    '''
    对匹配到的页面元素生成抓取规则
    '''
    rule=[]
    rule.append(gen_gather_rule_item(match_tag, is_end=True))
    for parent in match_tag.parents:
        if parent is None or parent.name=="selected_1161_inject_point":
            continue
        elif parent.has_attr("class") and parent["class"]=="selected_1161_inject_span":
            continue
        else:
            rule.append(gen_gather_rule_item(parent, is_end=False))
        if parent.name=='body':
            break
    rule.reverse()
    return rule

def gen_gather_rule_item(current_tag, is_end=False):
    '''
    对某个页面页面元素生成兄弟节点间的抓取规则（从兄弟节点中将需要的页面元素匹配出来）
    '''
    if type(current_tag) is NavigableString:
        print str(current_tag)
        if is_end:
            #有标红标记
            current_tag_children=current_tag.parent.parent.parent.children 
            index=0
            for current_tag_child in current_tag_children:
                print current_tag_child
                if type(current_tag_child) is Tag and current_tag_child.name=='selected_1161_inject_point':
                    break
                elif type(current_tag_child) is NavigableString and current_tag_child.strip()=='':
                    pass
                else:
                    index=index+1
            return [index, None, None]
        else:
            print list(current_tag.previous_siblings)
            index=len(list(current_tag.previous_siblings))
            return [index, None, None]
    else:
        if is_end:
            print str(current_tag.name)+str(current_tag.attrs)
            same_previous_siblings=current_tag.parent.parent.find_previous_siblings(name=current_tag.name, attrs=current_tag.attrs)#在前面的相同标签和属性的兄弟节点数
            index=len(same_previous_siblings)
            return [index, current_tag.name, current_tag.attrs]
        else:
            print str(current_tag.name)+str(current_tag.attrs)
            same_previous_siblings=current_tag.find_previous_siblings(name=current_tag.name, attrs=current_tag.attrs)#在前面的相同标签和属性的兄弟节点数
            index=len(same_previous_siblings)
            return [index, current_tag.name, current_tag.attrs]
def markRedYellowTag(soup, match_tag):
    '''
    对选中的元素做红框黄底的标记，有多个匹配到的元素时，标记当前选中中的一个
    '''
    match_tag_list=[]
    if hasattr(match_tag, '__iter__'):
        match_tag_list.extend(match_tag)
    else:
        match_tag_list.append(match_tag)
    for match_tag in match_tag_list:
        #NavigableString ok ，再检查Tag
        #需要改为dom结构去确认页面所选元素的位置。应对翻页
        match_tag_parent=match_tag.parent
        if match_tag_parent is not None and match_tag_parent.has_attr("class") and match_tag_parent["class"]=="selected_1161_inject_span":
            match_tag_parent["style"]="border:2px solid red;color:black;background-color:#ffff66;"
        else:
            selected_1161_inject_point = soup.new_tag("selected_1161_inject_point" )
            new_tag_mark = soup.new_tag("span" )
            new_tag_mark.attrs={"id":"selected_1161_inject_span", "class":"selected_1161_inject_span", "style":"border:2px solid red;color:black;background-color:#ffff66;"}        
            if type(match_tag) is NavigableString:
                match_tag.wrap(new_tag_mark).wrap(selected_1161_inject_point)
            else:
                for item in match_tag.strings:
                    item.wrap(new_tag_mark).wrap(selected_1161_inject_point)

def markYellowTag(soup, match_tag):
    '''
     对当前选中的所有元素做黄底的标记
    '''
    selected_1161_inject_point = soup.new_tag("selected_1161_inject_point" )
    new_tag_mark = soup.new_tag("span" )
    new_tag_mark.attrs={"id":"selected_1161_inject_span", "class":"selected_1161_inject_span", "style":"color:black;background-color:#ffff66;"}        
    if type(match_tag) is NavigableString:
        match_tag.wrap(new_tag_mark).wrap(selected_1161_inject_point)
    else:
        for item in match_tag.strings:
            item.wrap(new_tag_mark).wrap(selected_1161_inject_point)
            
def unmarkRedTag(match_tag):
    '''
    在手动调整页多个面选中元素时，去除上一个被选中元素的红框
    '''
    match_tag_parent=match_tag.parent
    if match_tag_parent is not None and match_tag_parent.has_attr("class") and match_tag_parent["class"]=="selected_1161_inject_span":
        match_tag_parent["style"]="color:black;background-color:#ffff66;"
    else:
        pass
        
# def unmarkRedTag(soup):
#     match_tag_list = soup.find_all(attrs={'class':'selected_1161_inject_span',})
#     for match_tag in match_tag_list:
#         match_tag.style="color:black;background-color:#ffff66;"

def selectedItemMarkColor(soup, match_tag):
    '''
    确认所选择的抓取元素后，清楚选择调整过程中产生的标记，给确认选择的元素背景标红
    '''
    #确认匹配的元素背景标红
    match_tag_parent=match_tag.parent
    if match_tag_parent is not None and match_tag_parent.has_attr("class") and match_tag_parent["class"]=="selected_1161_inject_span":
        match_tag_parent["style"]="color:black;background-color:red;"
    else:
        pass
    clearMarkColor(soup)
    
def clearMarkColor(soup):
    '''
    移除页面上颜色标记的元素，确认规则的元素除外（背景为red）
    '''
    #完成一次元素匹配，去除中间产生的选择调整标记（黄色标记）
    selected_1161_inject_point_list=soup.find_all('selected_1161_inject_point')
    for selected_1161_inject_point in selected_1161_inject_point_list:
        if selected_1161_inject_point.span is not None:
            selected_1161_inject_point_style=selected_1161_inject_point.span['style']
            if selected_1161_inject_point_style.find('color:black;background-color:red;')>=0:
                pass
            else:
                selected_1161_inject_point.span.unwrap()
        else:
            pass
    #移除selected_1161_inject_point标记 TODO
           
def find_tags(soup, selectedContents):
    '''
    通过selectedContents到soup中匹配出合符条件的节点。
    1、先用selectedContents中的第一个节点匹配，如果有多个匹配结果，再用之后的兄弟节点匹配。
    '''
    result_list = []
    need_delete_tag_list = []
    selectedContents="<html><body>"+selectedContents+"</body></html>"
    selected_soup = BeautifulSoup(selectedContents)
    selected_contents = selected_soup.body.contents
    if len(selected_contents)>0:
        current_tag = selected_contents[0]
        if type(current_tag) is NavigableString:
            result_list = soup.find_all(text=re.compile(current_tag.strip()))
        else:
            result_list = soup.find_all(name=current_tag.name, attrs=current_tag.attrs) #TODO 文本内容判断。
        for result in result_list:
            if equal_blur_text(result, current_tag):#有空串？？
                result_next_siblings = list(result.next_siblings)
                current_tag_next_siblings = list(current_tag.next_siblings)
                result_next_siblings_len = len(result_next_siblings)
                for index in range(len(current_tag_next_siblings)):
                    if result_next_siblings_len>index and not equal_blur_text(result_next_siblings[index], current_tag_next_siblings[index]):#TODO 无法删除所有不匹配的元素
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
        #选择的元素是NavigableString将其转化为有dom标签的结构，便于模式匹配。此处直接取父节点
        if type(current_tag) is NavigableString:
            for result in result_list:
                result = result.parent
    return result_list
    
def equal_blur_text(first_tag, second_tag):
    '''
    判断first_tag和second_tag两个标记Tag是否相等.
    模糊比较的地方是：1、first_tag的text包含second_tag的text即可。（只在最后的叶子节点NavigableString比较） 2、first_tag的子节点可以比second_tag多，但是顺序得一致。
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
        gatherData = GatherData()
        gatherData.soup =soup
        gatherData.src_soup =BeautifulSoup(soup.prettify())
        gather_data_dict[gather_site_id] = gatherData
        context = {"tgt_website": tgt_website, "gatherFrame_src": "/page/show_gather_site/"+str(gather_site_id), }
    else:
        #有部分网站有防iframe框架设置，如http://www.ablesky.com/lwschool，这类少数网站再改<input id="isAbleskyDomain" type="hidden" value="false">
        #html页面中一些元素的相对路径改为绝对路径
        base_url = tgt_website
        src_soup = BeautifulSoup(htmlsrc)#TODO
        relative_to_absolute_path(src_soup, {"link":"href", "script":"src", "img":"src", }, base_url)
        #
        soup = BeautifulSoup(htmlsrc)
        relative_to_absolute_path(soup, {"link":"href", "script":"src", "img":"src", }, base_url)
        #
        gatherData = GatherData()
        gatherData.soup =soup
        gatherData.src_soup =src_soup
        gatherData.web_site = tgt_website
        gather_data_dict[gather_site_id] = gatherData
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



