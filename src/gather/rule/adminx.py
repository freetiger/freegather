# -*- coding: utf-8 -*-
'''
Created on 2015年1月11日

@author: Administrator
'''
from django.utils.importlib import import_module
import xadmin

from gather.rule.models import PageInfo, LoopInfo, RegularMatch, BlockMatch


class BaseAdmin(object):
    #导出
    list_export = ()
    list_export_fixed = ('xlsx', 'xls', 'csv', 'xml', 'json')
    #数据版本控制，默认记录10个版本，可以调整。恢复删除的数据
    reversion_enable = True
        #相关模块操作
    use_related_menu=False
    
#     search_fileds = ('book__name', 'book__title', 'book__price', 'category')  # 设置搜索栏范围，如果有外键，要注明外键的哪个字段，双下划线
#     list_display = ('book', 'category')  # 在页面上显示的字段，若不设置则显示 models.py 中 __unicode__(self) 中所返回的值
#     list_display_links = ('category')  # 设置页面上哪个字段可单击进入详细页面
#     fields = ('category', 'book')  # 设置添加/修改详细信息时，哪些字段显示，在这里 remark 字段将不显示
   
    
#抓取任务
class BlockMatchAdmin(BaseAdmin):
    pass
#     list_display = ('job_name', 'thread_num', 'create_date', 'placeholders', 'placeholders_tips', 'scan_start', 'scan_end' )
#     #设置搜索框和其模糊搜索的范围
#     search_fields = ('job_name',) 
# #     list_display_links = ('create_date',)
#     show_detail_fields = ('job_name', )
#     #操作列表
#     #list_operate=['add', 'change', 'delete', 'detail', '<a href="www.github.com">github</a>', '<a href="http://www.github.com">http_github</a>'  ]
#     list_operate=['delete'
#                   , '<a href="/job/run_job_form/{{pk}}/" target="_blank">执行</a>'
#                   , '<a href="/job/scan/?_p_job__id__exact={{pk}}">扫描日志</a>', ]
#     list_editable = ('placeholders', )
    
    
#抓取任务
class RegularMatchAdmin(BaseAdmin):
    pass
#     list_display = ('job', 'scan_start', 'scan_end', 'is_finish', )
#     #设置搜索框和其模糊搜索的范围
#     search_fields = ('job__job_name',)
#     list_filter = ('job', )
#     list_operate=['delete'
#                   , '<a href="/job/scanresult/?_p_scan__id__exact={{pk}}">扫描结果</a>', ]
#     ordering = ('-scan_start',)
    
    
#抓取任务
class LoopInfoAdmin(BaseAdmin):
    pass
#     list_display = ('scan', 'scan_result', )
#     #设置搜索框和其模糊搜索的范围
#     #search_fields = ('job_name',)
#     list_filter = ('scan', )
#     ordering = ('pk',)
    
    
#抓取任务
class PageInfoAdmin(BaseAdmin):
    pass
#     list_display = ('scan', 'scan_result', )
#     #设置搜索框和其模糊搜索的范围
#     #search_fields = ('job_name',)
#     list_filter = ('scan', )
#     ordering = ('pk',)

xadmin.site.register(BlockMatch, BlockMatchAdmin)
xadmin.site.register(RegularMatch, RegularMatchAdmin)
xadmin.site.register(LoopInfo, LoopInfoAdmin)
xadmin.site.register(PageInfo, PageInfoAdmin)

#自定义插件导入   
import_module('plugins.operatelist')
import_module('plugins.export')

