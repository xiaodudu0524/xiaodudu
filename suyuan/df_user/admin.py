from django.contrib import admin
from models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','uemail','uphone']
    list_per_page = 10


admin.site.register(UserInfo,UserInfoAdmin)