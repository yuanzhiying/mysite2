#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'yuanzhiying'


from django.urls import path
from . import views

urlpatterns = [
    # /pools/
    path('', views.index, name='index'),
    # /pools/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /pools/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /pools/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]