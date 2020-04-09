from django.db import models

# Create your models here.
class Goods(models.Model):
    class Meta:
        db_table = 'record_storage'
        verbose_name = '库存查询'
        verbose_name_plural = '库存查询'
    name = models.CharField(max_length=128, null=False, verbose_name='物品名称')
    number1 = models.IntegerField(null=False, verbose_name='总入库数')
    number2 = models.IntegerField(null=False, verbose_name='总出库数')
    def __str__(self):
        return self.name


class Goods_out(models.Model):
    class Meta:
        db_table = 'record_out'
        verbose_name = '出库'
        verbose_name_plural = '出库'
    name = models.CharField(max_length=128, null=False, verbose_name='物品名称')
    number = models.IntegerField(null=False, verbose_name='物品数量')
    time = models.CharField(max_length=32, verbose_name='添加时间')
    user = models.CharField(max_length=32, null=False, verbose_name='操作用户')
    other = models.CharField(max_length=32, null=False, verbose_name='备注')
    repo = models.CharField(max_length=32, null=False, verbose_name='记录类型')

    def __unicode__(self):
        return self.name

class Goods_in(models.Model):
    class Meta:
        db_table = 'record_in'
        verbose_name = '入库'
        verbose_name_plural = '入库'
    name = models.CharField(max_length=128, null=False, verbose_name='物品名称')
    number = models.IntegerField(null=False, verbose_name='物品数量')
    time = models.CharField(max_length=32, verbose_name='添加时间')
    user = models.CharField(max_length=32, null=False, verbose_name='操作用户')
    other = models.CharField(max_length=32, null=False, verbose_name='备注')
    repo = models.CharField(max_length=32, null=False, verbose_name='记录类型')

    def __unicode__(self):
        return self.name