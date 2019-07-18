from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from fastrunner_collection import models
from fastrunner_collection import serializers
from fastrunner_collection.filter import DataFilter
from mysite import pagination
from mysite import pagination


class DataViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # 继承的GenericAPIView的queryset属性设置
    queryset = models.DataCollection.objects.all()
    # 继承的GenericAPIView的serializer_class属性设置
    serializer_class = serializers.DataSerializer

    pagination_class = pagination.MyCursorPagination
    # pagination_class = pagination.MyCursorPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # 设置过滤字段
    filter_fields = ('case_num', 'type')

    # filter_class = DataFilter
    search_fields = ('project',)

    # def get_queryset(self):
    #     p = self.request.query_params.get("id", 1)
    #     if p:
    #         return models.DataCollection.objects.filter(id=p)
    #     return models.DataCollection.objects.all()
