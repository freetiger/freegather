# -*- coding: utf-8 -*-
'''
Created on 2015年1月7日

@author: heyuxing
'''

from django.db import models

'''
这个规则提取了页面中从'<div class="content">\n<div class="info">'开始，到'<div class="content">\n<div class="info">'结束的一段html代码
'''
class BlockMatch(models.Model):
    result = models.CharField(max_length=32, verbose_name='结果名称')
    start_str = models.CharField(max_length=1024, verbose_name='起始字符串')
    end_str = models.CharField(max_length=1024, verbose_name='结束字符串')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return self.result
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='块匹配' 
        verbose_name_plural='块匹配'

'''
正则匹配
regular：用于匹配的正则表达式
result：正则匹配出的结果的名称，result1引用第一个结果，result2引用第二个结果，以此类推
'''
class RegularMatch(models.Model):
    result = models.CharField(max_length=32, verbose_name='结果名称')
    regulars = models.CharField(max_length=1024, verbose_name='正则表达式') #[]
    is_unique = models.BooleanField(default=True, verbose_name='唯一结果') #0表示抓全部的结果，这个值是1的话，只取第一个结果
    is_scroll = models.BooleanField(default=True, verbose_name='是否卷起') #"1",表示将抓取结果用||符号连接起来，生成一个整个的字符串，并用${lxstr}表示,这时不需加上表明位置的数字1
    omit_tags = models.CharField(max_length=1024, verbose_name='去除标记')#去除HTML标记，只保留内容： ['font','/font']表示匹配前过滤掉'font','/font'两个tag
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return self.result
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='正则匹配' 
        verbose_name_plural='正则匹配'
    
'''
循环抓取的规则
'''
class LoopInfo(models.Model):
    is_need_loop = models.BooleanField(default=True, verbose_name='循环抓取')
    loop_urls = models.TextField(default=[], verbose_name='循环的链接') #[]
    offset = models.IntegerField(default=1, verbose_name='偏移量')
    limit = models.IntegerField(default=0, verbose_name='最大偏移量')#小于等于0表示无限制
    step = models.IntegerField(default=1, verbose_name='步长')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return self.loop_urls
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='循环规则' 
        verbose_name_plural='循环规则'
    

class PageInfo(models.Model):
    urls = models.TextField(verbose_name='页面URL/源码')    #[]
    post_datas = models.TextField(verbose_name='POST数据')    #[]
    regular_matchs = models.ManyToManyField(RegularMatch, blank=True, verbose_name='正则匹配' )   # style_fields=['m2m_transfer' , ]
    block_match = models.ForeignKey(BlockMatch)   #
    loop_info = models.ForeignKey(LoopInfo)   #
    encoding = models.CharField(max_length=32, verbose_name='页面编码')
    is_need_loop = models.BooleanField(default=True, verbose_name='需要循环')
    encoding = models.CharField(max_length=32, verbose_name='页面编码')
    description = models.CharField(max_length=32, verbose_name='页面描述')
    is_end = models.BooleanField(default=False, verbose_name='抓取终止') #是否结束抓取，输出结果
    output_keys = models.CharField(max_length=1024, verbose_name='输出的结果')#需要输出的结果
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return self.urls
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='页面规则' 
        verbose_name_plural='页面规则'
        
        

    