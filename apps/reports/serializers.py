# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/5/14 20:21 
    
  @File : serializers.py
   
-------------------------------------------------
"""
from rest_framework import serializers

from .models import Reports


class ReportsModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ('update_time',)
        read_only_fields = ('name', 'count', 'result', 'success')
        extra_kwargs = {
            "create_time": {
                "read_only": True,
                "format": '%Y-%m-%d %H:%M:%S'
            },
            "name": {
                "read_only": True,
            },
            "html": {
                "write_only": True
            },
            "summary": {
                "write_only": True
            }

        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['result'] = '成功' if data.get('result') else '失败'
        return data
