from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    # 关联系统User，on_delete表示关联删除, related_name是反向查询的关键词
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                related_query_name="%(app_label)s_%(class)ss")
    telephone = models.CharField('手机号', max_length=20, blank=True)
    mod_date = models.DateTimeField(verbose_name='修改日期', auto_now=True)

    def __str__(self):
        return self.user
