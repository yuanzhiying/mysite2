#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'yuanzhiying'


from django.urls import path
from . import views

app_name = 'polls'  # 命名空间，为了区分不同的app，以便{% url %}能找到对应app的url
urlpatterns = [
    # /pools/
    path('', views.IndexView.as_view(), name='index'),
    # /pools/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /pools/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /pools/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]