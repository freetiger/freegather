# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: heyuxing
'''

from django.conf.urls import patterns, url
from gather.page import views
urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^show_gather_site/(?P<gather_site_id>[^/]+)/$', views.show_gather_site, name='show_gather_site'),
    url(r'^run_job_form/$', views.run_job_form, name='run_job_form'),
)


# from django.conf.urls import patterns, url
# from django.views.generic import DetailView, ListView
# from gather.job.models import Job,Scan,ScanResult
# 
# urlpatterns = patterns('',
#     url(r'^$',
#         ListView.as_view(
#             queryset=Job.objects.order_by('-create_date')[:5],
#             context_object_name='job_list',
#             template_name='gather/job/index.html'),
#         name='index'),
#     url(r'^(?P<pk>\d+)/$',
#         DetailView.as_view(
#             model=Job,
#             template_name='gather/job/detail.html'),
#         name='detail'),
#     url(r'^(?P<pk>\d+)/results/$',
#         DetailView.as_view(
#             model=Job,
#             template_name='gather/job/results.html'),
#         name='results'),
# #     url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
# )