# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/18 20:02 
    
  @File : validators.py
   
-------------------------------------------------
"""
from rest_framework import serializers

from projects.models import Projects
from interfaces.models import Interfaces
from envs.models import Envs


# def is_exist_project_id(data):
#     if not Projects.objects.filter(id=value).exists():
#         raise serializers.ValidationError("项目id不存在")
#
#
# def is_exist_interface_id(data):
#     if not Interfaces.objects.filter(id=value).exists():
#         raise serializers.ValidationError("接口id不存在")


class ManualValidateIsExist:
    def __init__(self, kw):
        self.kw = kw

    def __call__(self, value):
        if self.kw == "project":
            if not Projects.objects.filter(id=value).exists():
                raise serializers.ValidationError("项目id不存在")
        elif self.kw == "interface":
            if not Interfaces.objects.filter(id=value).exists():
                raise serializers.ValidationError("接口id不存在")
        elif self.kw == "env":
            if not Envs.objects.filter(id=value).exists():
                raise serializers.ValidationError("环境配置id不存在")
