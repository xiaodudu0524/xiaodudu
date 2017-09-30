#coding=utf-8
from django.shortcuts import render,HttpResponse
from models import *
from django.core.paginator import Paginator,Page
from django.utils.six import BytesIO
from django.http import JsonResponse,HttpResponseRedirect
import json
import qrcode
import os

# Create your views here.
def index(request):
    typelist = TypeInfo.objects.all()#
    #type1 是按默认的id，type11是按点击量
    type1 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type22 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type33 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    context = {'type1':type1,'type11':type11,'type2':type2,'type22':type22,'type3':type3,'type33':type33}
    return render(request,'df_shouye/index.html',context)

def list(request,tid,index,sort):
    #根据id拿到每个类型所对应的TypeInfo
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    #默认，最新
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    #根据点击量
    elif sort == '2':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    #将拿到的goods_list列表的进行分页
    paginator = Paginator(goods_list,24)
    page = paginator.page(int(index))
    context = {'title':typeinfo.ttitle,
               'page':page,
               'paginator':paginator,
               'typeinfo':typeinfo,
               'sort':sort,
               'news':news,
               }
    return render(request,'df_shouye/list.html',context)


#点击详情页面
def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick + 1
    goods.save()

    growimages = goods.growimage_set.all()
    fertilizers = goods.fertilizer_set.all()
    pesticides = goods.pesticide_set.all()
    environments = goods.environment_set.all()
    context = {'title': goods.gtype.ttitle, 'g': goods, 'environments':environments,'growimages': growimages, 'fertilizers': fertilizers,'pesticides':pesticides}
    return render(request, 'df_shouye/detail.html', context)

def env_handle(request):
    data = [['Date.UTC(2013,5,2)',0.7695],
            ['Date.UTC(2013,5,3)',0.7648],
            ['Date.UTC(2013,5,4)',0.7645],
            ['Date.UTC(2013,5,5)',0.7638],
            ['Date.UTC(2013,5,6)',0.7549]]

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')



#生成二维码
def generate_qrcode(request,data):
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream,content_type="image/png")
    return response

def data_1(request):
    id = request.GET.get('env_data_id')
    # print id
    goods = GoodsInfo.objects.get(pk=int(id))
    env = goods.environment_set.all()[0]
    env_path = str(env.air_temp)    #airtemp/123_nTldbzy.txt
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print BASE_DIR   #/home/shixianzhang/project/suyuan
    sep = BASE_DIR,'static',env_path
    path = '/'.join(sep)
    file = open(path)
    arr = []
    while 1:
        lines = file.readline()
        if not lines:
            break
        line = lines.splitlines()
        data = line[0].split(' ')
        arr.append(data)
    json_data = json.dumps(arr)
    return HttpResponse(json_data,content_type='application/json')

def data_2(request):
    id = request.GET.get('env_data_id')
    # print id
    goods = GoodsInfo.objects.get(pk=int(id))
    env = goods.environment_set.all()[0]
    env_path = str(env.air_hum)    #airtemp/123_nTldbzy.txt
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print BASE_DIR   #/home/shixianzhang/project/suyuan
    sep = BASE_DIR,'static',env_path
    path = '/'.join(sep)
    file = open(path)
    arr = []
    while 1:
        lines = file.readline()
        if not lines:
            break
        line = lines.splitlines()
        data = line[0].split(' ')
        arr.append(data)
    json_data = json.dumps(arr)
    return HttpResponse(json_data,content_type='application/json')

def data_3(request):
    id = request.GET.get('env_data_id')
    # print id
    goods = GoodsInfo.objects.get(pk=int(id))
    env = goods.environment_set.all()[0]
    env_path = str(env.soil_temp)    #airtemp/123_nTldbzy.txt
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print BASE_DIR   #/home/shixianzhang/project/suyuan
    sep = BASE_DIR,'static',env_path
    path = '/'.join(sep)
    file = open(path)
    arr = []
    while 1:
        lines = file.readline()
        if not lines:
            break
        line = lines.splitlines()
        data = line[0].split(' ')
        arr.append(data)
    json_data = json.dumps(arr)
    return HttpResponse(json_data,content_type='application/json')


def data_4(request):
    id = request.GET.get('env_data_id')
    # print id
    goods = GoodsInfo.objects.get(pk=int(id))
    env = goods.environment_set.all()[0]
    env_path = str(env.soil_hum)    #airtemp/123_nTldbzy.txt
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print BASE_DIR   #/home/shixianzhang/project/suyuan
    sep = BASE_DIR,'static',env_path
    path = '/'.join(sep)
    file = open(path)
    arr = []
    while 1:
        lines = file.readline()
        if not lines:
            break
        line = lines.splitlines()
        data = line[0].split(' ')
        arr.append(data)
    json_data = json.dumps(arr)
    return HttpResponse(json_data,content_type='application/json')