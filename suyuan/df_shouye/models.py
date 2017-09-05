#coding=utf-8
from django.db import models
from tinymce.models import HTMLField



class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gintroduce = HTMLField(default="",null=True)
    gcontent = HTMLField(null=True)
    gpic = models.ImageField(upload_to='goods')
    company_name = models.CharField(max_length=20,default="")
    company_address = models.CharField(max_length=50,default="")
    company_president = models.CharField(max_length=20,default="")
    company_detail = HTMLField(null=True)
    gtime = models.DateTimeField()
    gclick = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    gtype = models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.gtitle.encode('utf-8')

#农作物生长周期图片
class GrowImage(models.Model):
    growimage = models.ImageField(upload_to='growimages')
    beizhu = models.CharField(max_length=50)
    growtype = models.ForeignKey(GoodsInfo)


#肥料使用表
class Fertilizer(models.Model):
    usetime = models.DateTimeField()
    fertilizername = models.CharField(max_length=50)
    leixing = models.CharField(max_length=50)
    yongliang = models.CharField(max_length=50)
    pingpai = models.CharField(max_length=50)
    gongyingshang = models.CharField(max_length=50)
    ftype = models.ForeignKey(GoodsInfo)


class Pesticide(models.Model):
    useTime = models.DateTimeField()
    pesticidename = models.CharField(max_length=50)
    yongLiang = models.CharField(max_length=50)
    pingPai = models.CharField(max_length=50)
    gongYingshang = models.CharField(max_length=50)
    pType = models.ForeignKey(GoodsInfo)