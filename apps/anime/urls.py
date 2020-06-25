#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 未衬

# path 这个方法是专门定义网站地址的
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('anime/', views.Anime, name='anime'),
    path('ps/', views.jf_cl, name='ps'),
    path('dr/', views.jz_gl, name='dr'),
]
