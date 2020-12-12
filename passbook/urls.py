# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'passbook'

urlpatterns = [
    path('', views.PassBookView.as_view(), name='passbook_index'),
]
