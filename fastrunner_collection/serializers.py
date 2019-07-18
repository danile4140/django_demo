#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/7/16

@author: danny.deng
@des: 
"""
from rest_framework import serializers

from fastrunner_collection import models


class DataSerializer(serializers.ModelSerializer):
    """序列化"""

    class Meta:
        model = models.DataCollection
        fields = ['elapsed_time', 'start_time', 'type', 'project']

