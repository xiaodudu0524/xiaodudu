#coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GrowImageAdmin(admin.TabularInline):
    #max_num = 3 #设置最多有几个框

    model = GrowImage

class FertilizerAdmin(admin.TabularInline):
    model = Fertilizer

class PesticideAdmin(admin.TabularInline):
    model = Pesticide


class GoodsInfoAdmin(admin.ModelAdmin):

    inlines = [GrowImageAdmin,FertilizerAdmin,PesticideAdmin]
    list_per_page = 10
    list_display = ['id','gtitle','gtime','gclick','gtype']
    search_fields = ['gtitle']




admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)

