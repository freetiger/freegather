# -*- coding: utf-8 -*-
'''
Created on 2015年1月7日

@author: heyuxing
'''
'''
这个规则提取了页面中从'<div class="content">\n<div class="info">'开始，到'<div class="content">\n<div class="info">'结束的一段html代码
'''


class BlockMatch(object):
    result = "" #models.CharField(max_length=32, verbose_name='结果名称')
    start_str = ""  #models.CharField(max_length=1024, verbose_name='起始字符串')
    end_str = ""    #models.CharField(max_length=1024, verbose_name='结束字符串')

'''
正则匹配
regular：用于匹配的正则表达式
result：正则匹配出的结果的名称，result1引用第一个结果，result2引用第二个结果，以此类推
'''
class RegularMatch(object):
    result = "" #models.CharField(max_length=32, verbose_name='结果名称')
    regulars = []   #models.CharField(max_length=1024, verbose_name='正则表达式') #[]
    is_unique = "0"   #models.BooleanField(default=True, verbose_name='唯一结果') #0表示抓全部的结果，这个值是1的话，只取第一个结果
    is_scroll = "0"   #models.BooleanField(default=True, verbose_name='是否卷起') #"1",表示将抓取结果用||符号连接起来，生成一个整个的字符串，并用${lxstr}表示,这时不需加上表明位置的数字1
    omit_tags = []    #models.CharField(max_length=1024, verbose_name='去除标记')#去除HTML标记，只保留内容： ['font','/font']表示匹配前过滤掉'font','/font'两个tag
  
class LoopInfo(object):  
    is_need_loop = "0"    #models.BooleanField(default=True, verbose_name='需要循环')
    loop_urls = []  #models.CharField(max_length=1024, verbose_name='循环URL')
    offset = "1"  #计数起点为1，第一个值下标为1
    limit = "0"
    step = "1"

class PageInfo(object):
    urls = []   #models.TextField(verbose_name='页面URL/源码')    #[]
    regular_matchs = [] #models.ManyToManyField(RegularMatch, blank=True, verbose_name='正则匹配' )   # style_fields=['m2m_transfer' , ]
    block_match = None  #models.ForeignKey(BlockMatch)   #
    encoding = "GBK"   #models.CharField(max_length=32, verbose_name='页面编码')
    description = ""    #models.CharField(max_length=32, verbose_name='页面描述')
    is_end = "0"  #models.BooleanField(default=True, verbose_name='结束抓取') #是否结束抓取，输出结果
    output_keys = []    #models.CharField(max_length=1024, verbose_name='输出的结果')#需要输出的结果
    loop_info = None
    post_datas = {}  #url 请求post的数据
    

    