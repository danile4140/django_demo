from django.db import models


# Create your models here.


class DataCollection(models.Model):
    class Meta:
        verbose_name = "接口自动化数据收集"
        verbose_name_plural = verbose_name
        db_table = "Data"

    TYPE = (
        (1, "调试"),
        (2, "异步"),
        (3, "定时"),
        (4, "auto")
    )
    case_num = models.IntegerField(verbose_name="用例数", default=0, null=False)
    case_pass_num = models.IntegerField(verbose_name="用例通过数", default=0, null=False)
    case_fail_num = models.IntegerField(verbose_name="用例失败数", default=0, null=False)
    case_skip_num = models.IntegerField(verbose_name="用例跳过数", default=0, null=False)
    api_pass_num = models.IntegerField(verbose_name="API通过数", default=0, null=False)
    api_fail_num = models.IntegerField(verbose_name="API失败数", default=0, null=False)
    api_error_num = models.IntegerField(verbose_name="API异常数", default=0, null=False)
    elapsed_time = models.IntegerField(verbose_name="执行时间", null=False)
    start_time = models.FloatField(verbose_name="开始时间", null=False)
    type = models.PositiveSmallIntegerField(verbose_name="类型", choices=TYPE, null=False)
    project = models.IntegerField(verbose_name="项目ID", null=False)
