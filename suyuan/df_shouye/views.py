#coding=utf-8
from django.shortcuts import render,HttpResponse
from models import *
from django.core.paginator import Paginator,Page
from django.utils.six import BytesIO
import qrcode
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


    context = {'title':goods.gtype.ttitle,'g':goods,'growimages':growimages,'fertilizers':fertilizers}
    return render(request,'df_shouye/detail.html',context)




#生成二维码
def generate_qrcode(request,data):
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream,content_type="image/png")
    return response

