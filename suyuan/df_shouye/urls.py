from django.conf.urls import include, url
import views
urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^qrcode/(.+)/$',views.generate_qrcode,name='qrcode'),
    url('^(\d+)/$', views.detail),

]