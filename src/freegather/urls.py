# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microscope.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(xadmin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^job/', include('gather.job.urls', namespace="job")),
    url(r'^page/', include('gather.page.urls', namespace="page")),
)
