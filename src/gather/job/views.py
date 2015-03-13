# -*- coding: utf-8 -*-
'''
Created on 2014年10月20日

@author: heyuxing
'''

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from gather.job.models import Job, WeixinArticleListScan, WeixinArticleContentScan, WeixinArticle

from gather.job.forms import RunJobForm
from django.shortcuts import render_to_response
from gather.script.grabber import Grabber


# from django.http import HttpResponse
def index(request):
    job_list = Job.objects.all().order_by('-create_date')[:5]
    context = {'job_list': job_list}
    return render(request, 'gather/job/index.html', context)
 
def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {'job': job}
    return render(request, 'gather/job/detail.html', context)
 
def results(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'gather/job/results.html', {'job': job})

def saveOrUpdate(request, job_id):
    if job_id is not None:
        job = get_object_or_404(Job, pk=job_id)
    else:
        job = Job()
    if job is not Http404:
        job.job_name = request.POST['job_name']
#         job.get_rules = request.POST['get_rules']
#         job.placeholders = request.POST['placeholders']
#         job.thread_num = request.POST['thread_num']
        job.save()
        
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('job:detail', args=(job.id,)))

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def runJobForm(request, job_id):
    if request.method == 'POST':
        form = RunJobForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            print form
            job_name = form.get("job_name", "")
            get_rules = form.get("get_rules", "")
            placeholders = eval(form.get("placeholders", ""))
            thread_num = int(form.get("thread_num", 1))
            Grabber().startscan(job_id=job_id, job_name=job_name, get_rules=get_rules, placeholders=placeholders, thread_num=thread_num)
            #from gather.script.weixin_public import scan_article_list
            #scan_article_list()
            return HttpResponseRedirect('/job')
    else:
        job = Job.objects.get(pk=job_id)
        if job:
            form = RunJobForm(
                              initial={'job_name': job.job_name, 
                                       'get_rules': job.get_rules, 
                                       'placeholders': job.placeholders, 
                                       'thread_num': job.thread_num, 
                                       'create_date': job.create_date, 
                                       'placeholders_tips': Job.placeholders_tips(job), 
                                       }
                              )
        else:
            form = RunJobForm()
    return render_to_response('gather/job/run_job_form.html', {'form': form, 'base_template': 'xadmin/base.html'})


def runWeixinArticleListScan(request, weixin_scan_id):
    weixinArticleListScan = WeixinArticleListScan.objects.get(pk=weixin_scan_id)
    weixin_info = weixinArticleListScan.weixin_info
    weixin_name = weixin_info.weixin_name
    if weixin_name is None or weixin_name.strip()=="":
        weixin_name = weixin_info.weixin_no
    if weixin_name is None or weixin_name.strip()=="":
        weixin_name = weixin_info.openid
    html = "<html><body>%s 扫描结束.</body></html>" % weixin_name
    #
    from gather.script.weixin_public import scan_article_list
    scan_article_list(weixinArticleListScan.job_id, weixin_info.openid)
    return HttpResponse(html)

def runWeixinArticleContentScan(request, weixin_scan_id):
    weixinArticleContentScan = WeixinArticleContentScan.objects.get(pk=weixin_scan_id)
    weixin_info = weixinArticleContentScan.weixin_info
    weixin_name = weixin_info.weixin_name
    if weixin_name is None or weixin_name.strip()=="":
        weixin_name = weixin_info.weixin_no
    if weixin_name is None or weixin_name.strip()=="":
        weixin_name = weixin_info.openid
    html = "<html><body>%s 扫描结束.</body></html>" % weixin_name
    #
    from gather.script.weixin_public import scan_article_content
    scan_article_content(weixinArticleContentScan.job_id, weixinArticleContentScan.weixin_article_list_scan_id)
    return HttpResponse(html)

def testWeixinArticleShow(request):
    context = {}
    return render(request, 'gather/job/wenzhang.html', context)

def weixinArticleShow(request, weixin_article_id):
    weixinArticle = WeixinArticle.objects.get(pk=weixin_article_id)
    return HttpResponse(weixinArticle.content)



