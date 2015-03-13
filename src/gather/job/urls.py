# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: heyuxing
'''

from django.conf.urls import patterns, url
from gather.job import views
urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/results/
    url(r'^run_job_form/(?P<job_id>\d+)/$', views.runJobForm, name='run_job_form'),
    # ex: /polls/5/
    url(r'^(?P<job_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<job_id>\d+)/results/$', views.results, name='results'),
    url(r'^run_weixin_article_list_scan/(?P<weixin_scan_id>\d+)/$', views.runWeixinArticleListScan, name='run_weixin_article_list_scan'),
    url(r'^run_weixin_article_content_scan/(?P<weixin_scan_id>\d+)/$', views.runWeixinArticleContentScan, name='run_weixin_article_content_scan'),
    url(r'^test_weixin_article_show/$', views.testWeixinArticleShow, name='test_weixin_article_show'),
    url(r'^weixin_article_show/(?P<weixin_article_id>\d+)/$', views.weixinArticleShow, name='weixin_article_show'),
    # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
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