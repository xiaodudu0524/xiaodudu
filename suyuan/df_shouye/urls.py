from django.conf.urls import include, url
import views
urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^qrcode/(.+)/$',views.generate_qrcode,name='qrcode'),
    url(r'^(\d+)/$', views.detail),
    url(r'^env_handle/$',views.env_handle),
    url(r'^data_1/',views.data_1),
    url(r'^data_2/',views.data_2),
    url(r'^data_3/',views.data_3),
    url(r'^data_4/',views.data_4),
]