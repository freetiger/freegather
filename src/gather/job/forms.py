# -*- coding: utf-8 -*-
'''
Created on 2014年11月10日

@author: heyuxing
'''
from django import forms

class RunJobForm(forms.Form):
    job_name = forms.CharField(max_length=256,)
    get_rules = forms.CharField(widget=forms.Textarea, )
    placeholders = forms.CharField(max_length=256, )
    thread_num = forms.IntegerField(required=False)
    create_date = forms.DateTimeField( )
    placeholders_tips = forms.CharField()