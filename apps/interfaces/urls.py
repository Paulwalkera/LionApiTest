# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/4/26 21:37 
    
  @File : urls.py
   
-------------------------------------------------
"""
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'interfaces', views.InterfaceViewSet)

urlpatterns = [
]

urlpatterns += router.urls
