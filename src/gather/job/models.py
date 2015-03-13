# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: hyx
'''

import re

from django.db import models
from __builtin__ import super


class Job(models.Model):
    job_name = models.CharField(max_length=256, verbose_name='任务名称')
    get_rules = models.TextField(verbose_name='任务规则')
    placeholders = models.CharField(max_length=256, blank=True, verbose_name='规则占位符')
    thread_num = models.IntegerField(default=1, verbose_name='并发线程数')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def placeholders_tips(self):
        tips=[]
        placeholders_regular = re.compile(r'\{\{([^}]*)\}\}')
        placeholders = placeholders_regular.findall(self.get_rules)
        
        for placeholder in placeholders:
            tips.append(placeholder)
        return tips
    placeholders_tips.short_description = "规则占位符"
    placeholders_tips.allow_tags = True
    placeholders_tips.is_column = True
    
    def scan_start(self):
        last_scan = Scan.objects.filter(job_id=self.pk).order_by("-scan_start")[0:1]
        if last_scan :
            return last_scan[0].scan_start
        else:
            return ""
    scan_start.short_description = "开始时间"
    scan_start.allow_tags = True
    scan_start.is_column = True
                
    def scan_end(self):
        last_scan = Scan.objects.filter(job_id=self.pk).order_by("-scan_start")[0:1]
        if last_scan and last_scan[0].scan_end>last_scan[0].scan_start:
            return last_scan[0].scan_end
        else:
            return ""
    scan_end.short_description = "结束时间"
    scan_end.allow_tags = True
    scan_end.is_column = True
    
    def __unicode__(self):
        return self.job_name
    
    class Meta:
        ordering = ['job_name']
        verbose_name='抓取任务' 
        verbose_name_plural='抓取任务'
        
    def save(self):
        from freegather.settings import BASE_DIR
        job_save_log = BASE_DIR+"/gather/script/job_save_log.py"
        outputfile = open(job_save_log,"a")
        outputfile.write("#") 
        outputfile.write(self.job_name) 
        outputfile.write("\t")
        outputfile.write(self.placeholders)
        outputfile.write("\t")
        outputfile.write(str(self.thread_num))
        outputfile.write("\t")
        outputfile.write(str(self.create_date))
        outputfile.write("\n")
        outputfile.write(self.get_rules)
        outputfile.write("\n")
        outputfile.write("\n")
        outputfile.close()
        super(Job, self).save()
    
class Scan(models.Model):
    job = models.ForeignKey(Job)
    job_name = models.CharField(max_length=256, verbose_name='任务名称')
    get_rules = models.TextField(verbose_name='任务规则')
    placeholders = models.CharField(max_length=256, blank=True, verbose_name='规则占位符')
    thread_num = models.IntegerField(default=1, verbose_name='并发线程数')
    scan_start = models.DateTimeField(blank=True, null=True, verbose_name='开始时间')
    scan_end = models.DateTimeField(blank=True, null=True, verbose_name='结束时间')
    is_finish = models.BooleanField(default=True, verbose_name='是否完成')
#     is_finish.editable=False #是否显示出来可以编辑
    
    def __unicode__(self):
        return self.job_name
    
    class Meta:
        ordering = ['scan_start']
        verbose_name='扫描任务' 
        verbose_name_plural='扫描任务'

class ScanResult(models.Model):
    scan = models.ForeignKey(Scan)
    scan_result = models.TextField()
    
    def __unicode__(self):
        return self.scan_result
    
    class Meta:
        ordering = ['scan']
        verbose_name='扫描结果' 
        verbose_name_plural='扫描结果'
   
class WeixinInfo(models.Model):
    weixin_name = models.CharField(max_length=256, verbose_name='微信名')
    weixin_no = models.CharField(max_length=256, verbose_name='微信号')
    openid = models.CharField(max_length=256, verbose_name='微信openid')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')     
    
    def __unicode__(self):
        return self.weixin_name
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='微信列表' 
        verbose_name_plural='微信列表'
        
class WeixinArticleListScan(models.Model):
    weixin_info = models.ForeignKey(WeixinInfo, verbose_name='微信号信息')
    job = models.ForeignKey(Job, verbose_name='文章列表抓取')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return str(self.weixin_info)
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='文章列表' 
        verbose_name_plural='文章列表'
        
class WeixinArticleContentScan(models.Model):
    weixin_info = models.ForeignKey(WeixinInfo, verbose_name='微信号信息')
    weixin_article_list_scan = models.ForeignKey(WeixinArticleListScan, verbose_name='文章列表抓取')
    job = models.ForeignKey(Job, verbose_name='文章内容抓取')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return str(self.weixin_info)
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='文章内容' 
        verbose_name_plural='文章内容'
        
class WeixinArticle(models.Model):
    weixin_info = models.ForeignKey(WeixinInfo, verbose_name='微信号信息')
    title = models.CharField(max_length=256, verbose_name='文章标题')
    url = models.CharField(max_length=1024, verbose_name='文章源URL')
    content = models.TextField(verbose_name='文章内容')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    
    def __unicode__(self):
        return str(self.weixin_info)+": "+self.title
    
    class Meta:
        ordering = ['-create_date']
        verbose_name='微信文章' 
        verbose_name_plural='微信文章'
        
        
    
    