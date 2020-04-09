from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from . import models
from django.utils import timezone
from django.db.models import Q


# Create your views here.
def index(request):
    # return HttpResponse('你好世界')
    goods = models.Goods.objects.all()
    return render(request, 'summer/index.html', {'goods': goods})


def add_new(request):
    if request.method == "POST":
        name2 = request.POST.get('name')
        number = request.POST.get('number')
        time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S") #取当地时间 再strftime格式化
        user = request.POST.get('user')
        other = request.POST.get('other')
        try:
            storage_name = models.Goods.objects.get(name = name2)   #get返回的是一个对象，如果在数据库查不到值，会抛异常，用models.DoesN抛
            if storage_name:
                try:
                    # storage_num1 = models.Goods.objects.get(storage_name)
                    storage_name.number1 = storage_name.number1 + int(number) #库存中存在货物更新库存数量
                    storage_name.save()
                    new_goods = models.Goods_in()
                    new_goods.name = name2
                    new_goods.number = number
                    new_goods.time = time
                    new_goods.user = user
                    new_goods.other = other
                    new_goods.repo = "入库"
                    new_goods.save()
                    message = "入库成功"
                    return render(request, 'summer/add_new.html', {'message': message})
                except Exception as e:
                    message = e
                    return render(request, 'summer/add_new.html', {'message': message})
            else:
                message = "此“入库信息”未在库存信息中，请在库存查询页添加后再执行该操作"
                return render(request, 'summer/add_new.html', {'message': message})
        except models.Goods.DoesNotExist:
            message = "此“入库信息”未在库存信息中，请在库存查询页添加后再执行该操作"
            return render(request, 'summer/add_new.html', {'message': message})
    else:
        message = "请正确输入信息"
        return render(request, 'summer/add_new.html', {'message': message})


def out_new(request):
    if request.method == "POST":
        name2 = request.POST.get('name')
        number = request.POST.get('number')
        time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
        user = request.POST.get('user')
        other = request.POST.get('other')
        try:
            storage_name = models.Goods.objects.filter(name=name2)
            if storage_name:
                try:
                    storage_name.number2 = storage_name.number2 + int(number)
                    storage_name.save()
                    new_goods = models.Goods_out()
                    new_goods.name = name2
                    new_goods.number = number
                    new_goods.time = time
                    new_goods.user = user
                    new_goods.other = other
                    new_goods.repo = "出库"
                    new_goods.save()
                    message = "出库成功"
                    return render(request, 'summer/out_new.html', {'message': message})
                except Exception as e:
                    message = e
                    return render(request, 'summer/out_new.html', {'message': message})
            else:
                message = "此“出库信息”未在库存信息中，请在库存查询页添加后再执行该操作"
                return render(request, 'summer/out_new.html', {'message': message})
        except models.Goods.DoesNotExist:
            message = "此“出库信息”未在库存信息中，请在库存查询页添加后再执行该操作"
            return render(request, 'summer/out_new.html', {'message': message})
    else:
        message = "请输入出库信息"
        return render(request, 'summer/out_new.html', {'message': message})


def record_query(request):
    if request.method == "POST":
        kind = request.POST.get('kind')
        names = request.POST.get('name')
        if str(kind) == "0" and (names is None or names == "") :   #查全部记录
            try:
                infos = models.Goods_out.objects.all().order_by("-time")
                message = "这是出库记录"
                return render(request, 'summer/record_query.html', {'infos': infos})
            except Exception as e:
                infos = e
                return render(request, 'summer/record_query.html', {'infos': infos})
        elif str(kind) == "0" and names:  #查货物相关记录
            try:
                infos = models.Goods_out.objects.filter(name=names).order_by("-time")
                message = "这是出库记录"
                return render(request, 'summer/record_query.html', {'infos': infos})
            except Exception as e:
                infos = e
                return render(request, 'summer/record_query.html', {'infos': infos})
        elif str(kind) == "1" and (names is None or names == ""):
            try:
                infos = models.Goods_in.objects.all().order_by("-time")
                message = "这是入库记录"
                return render(request, 'summer/record_query.html', {'infos': infos})
            except Exception as e:
                infos = e
                return render(request, 'summer/record_query.html', {'infos': infos})
        elif str(kind) == "1" and names:
            try:
                infos = models.Goods_in.objects.filter(name = names).order_by("-time")
                message = "这是入库记录"
                return render(request, 'summer/record_query.html', {'infos': infos})
            except Exception as e:
                infos = e
                return render(request, 'summer/record_query.html', {'infos': infos})
        else:
            message = "请选择查询类型"
            return render(request, 'summer/record_query.html', {'message': message})

    else:
        message = "请输入正确内容"
        return render(request, 'summer/record_query.html', {'message': message})

def storage_add(request):
    if request.method == "POST":
        nname = request.POST.get('name')
        if nname:
            try:
                stadd = models.Goods()
                stadd.name = nname
                stadd.number1 = int(0)
                stadd.number2 = int(0)
                stadd.save()
                message = "库存信息添加成功"
                # return render(request, 'summer/storage.html', {'message': message})
                good_show = models.Goods.objects.all()
                return render(request, 'summer/storage.html', {'goods': good_show})
            except Exception as e:
                message = e
                return render(request, 'summer/storage.html', {'message': e})
        else:
            message = "输入信息不存在"
            return render(request, 'summer/storage.html', {'message': message})
    else:
        message = "输入信息有误"
        return render(request, 'summer/storage.html', {'message': message})

def storage_show(request):
    good_show = models.Goods.objects.all()
    return render(request, 'summer/storage.html', {'goods': good_show})

def show(request, good_id):
    good = models.Foods.objects.get(pk=good_id)
    return render(request, 'summer/show.html', {'good': good})
