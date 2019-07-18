#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/7/17

@author: danny.deng
@des: 
"""
from django_filters import FilterSet, NumberFilter

from fastrunner_collection.models import DataCollection


class DataFilter(FilterSet):
    min_case = NumberFilter(name='case_num', lookup_expr='gte')
    max_case = NumberFilter(name='case_num', lookup_expr='lt')

    class Meta:
        model = DataCollection
        fields = ['min_case', 'max_case']
