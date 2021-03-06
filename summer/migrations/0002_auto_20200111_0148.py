# Generated by Django 2.2.6 on 2020-01-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='物品名称')),
                ('number1', models.IntegerField(verbose_name='总入库数')),
                ('number2', models.IntegerField(verbose_name='总出库数')),
            ],
            options={
                'verbose_name': '库存查询',
                'verbose_name_plural': '库存查询',
                'db_table': 'record_storage',
            },
        ),
        migrations.CreateModel(
            name='Goods_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='物品名称')),
                ('number', models.IntegerField(verbose_name='物品数量')),
                ('time', models.CharField(max_length=32, verbose_name='添加时间')),
                ('user', models.CharField(max_length=32, verbose_name='操作用户')),
                ('other', models.CharField(max_length=32, verbose_name='备注')),
                ('repo', models.CharField(max_length=32, verbose_name='记录类型')),
            ],
            options={
                'verbose_name': '入库',
                'verbose_name_plural': '入库',
                'db_table': 'record_in',
            },
        ),
        migrations.CreateModel(
            name='Goods_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='物品名称')),
                ('number', models.IntegerField(verbose_name='物品数量')),
                ('time', models.CharField(max_length=32, verbose_name='添加时间')),
                ('user', models.CharField(max_length=32, verbose_name='操作用户')),
                ('other', models.CharField(max_length=32, verbose_name='备注')),
                ('repo', models.CharField(max_length=32, verbose_name='记录类型')),
            ],
            options={
                'verbose_name': '出库',
                'verbose_name_plural': '出库',
                'db_table': 'record_out',
            },
        ),
        migrations.DeleteModel(
            name='Foods',
        ),
    ]
