# -*- coding: utf-8 -*-
'''
Created on 2014年12月22日

@author: heyuxing
'''
from django.core.urlresolvers import reverse
from django.utils.encoding import force_unicode
from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView

class ListoperatePlugin(BaseAdminPlugin):

    '''
    获得“操作列”的操作设置，在adminx.py中设置
    list_operate=['add', 'change', 'delete', 'detail', '<a href="www.github.com">github</a>', '<a href="http://www.github.com">http_github</a>'  ]
    'add', 'change', 'delete', 'detail', ：这四个值是model的“增加”、“修改”、“删除”、“详情”四个常用操作
    {{pk}}这类为占位符，需要替换为实例中值
    其他值为自定义字符串，原样显示
    如果字符串中有<a>标签，相对路径会自动增加当前页面的链接前缀，不想要自动增加的前缀请加上协议名（如：http://）
    list_operate_delimiter设置各个操作之间的分隔符，默认为一个空格符
    '''
    list_operate = []
    list_operate_delimiter = " "
    
    def operate_list(self, instance):
        def get_placeholders(string):
            import re
            tips=[]
            placeholders_regular = re.compile(r'\{\{([^}]*)\}\}')
            placeholders = placeholders_regular.findall(string)
            for placeholder in placeholders:
                tips.append(placeholder)
            return tips
        #查看BaseAdminPlugin的属性， 可以使用dir查看dir(self.opts)
        app_name = self.admin_site.app_name #应用名称
        app_label = self.opts.app_label #包名
        model_name = force_unicode(self.opts.model_name)    #模块名
        pk = instance.pk #主键id
        
        result = ""
        if self.list_operate:
            for operate in self.list_operate:
                if 'add'==operate:
                    result += "<a href='"+reverse('%s:%s_%s_add' % (app_name, app_label, model_name))+"'>增加</a>" + self.list_operate_delimiter
                elif 'change'==operate:
                    result += "<a href='"+reverse('%s:%s_%s_change' % (app_name, app_label, model_name), args=(pk, ))+"'>修改</a>" + self.list_operate_delimiter
                elif 'delete'==operate:
                    result += "<a href='"+reverse('%s:%s_%s_delete' % (app_name, app_label, model_name), args=(pk, ))+"'>删除</a>" + self.list_operate_delimiter
                elif 'detail'==operate:
                    result += "<a href='"+reverse('%s:%s_%s_detail' % (app_name, app_label, model_name), args=(pk, ))+"'>详情</a>" + self.list_operate_delimiter
                else:
                    placeholders = get_placeholders(operate)
                    for placeholder in placeholders:
                        if hasattr(instance, placeholder): #检查实例是否有这个属性 TODO 区分类型
                            operate = operate.replace("{{"+placeholder+"}}",str(getattr(instance, placeholder)))
                        else:
                            operate = operate.replace("{{"+placeholder+"}}",placeholder)
                    result += operate + self.list_operate_delimiter
        
        return result
    
    operate_list.short_description = u'操作'
    operate_list.allow_tags = True
    operate_list.allow_export = False
    operate_list.is_column = False

    '''
    展示数据的表格设置新增加的一列
    '''
    def get_list_display(self, list_display):
        if len(self.list_operate):
            list_display.append('operate_list')
            self.admin_view.operate_list = self.operate_list
        return list_display

site.register_plugin(ListoperatePlugin, ListAdminView)
