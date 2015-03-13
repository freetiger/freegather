# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: hyx
'''
from django.contrib import admin
from gather.job.models import Job,Scan,ScanResult

class ScanInline(admin.TabularInline):    #StackedInline
    model = Scan
    extra = 0

class JobAdmin(admin.ModelAdmin):
    # ...
    list_display = ('job_name', 'get_rules', 'placeholders_tips', 'placeholders', 'thread_num', 'create_date')
    #
    list_filter = ['create_date']
    search_fields = ['job_name']
    ordering = ('-create_date',)
    list_per_page = 10
    inlines = [ScanInline]
    
class ScanResultInline(admin.TabularInline):    #StackedInline
    model = ScanResult
    extra = 0
    
class ScanAdmin(admin.ModelAdmin):
    list_display = ('job', 'scan_start', 'scan_end', 'is_finish')
    #
    list_filter = ['scan_start']
    search_fields = ['job']
    ordering = ('-scan_start',)
    list_per_page = 10
    inlines = [ScanResultInline]
    
class ScanResultAdmin(admin.ModelAdmin):
    list_display = ('scan', 'scan_result')
    #
    search_fields = ['scan_result']
    ordering = ('-scan',)
    list_per_page = 10
    
admin.site.register(Job, JobAdmin)
admin.site.register(Scan, ScanAdmin)
admin.site.register(ScanResult, ScanResultAdmin)