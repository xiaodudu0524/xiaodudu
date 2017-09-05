from django.conf.urls import include, url
import views
urlpatterns =[
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exist/$',views.register_exist),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.activeuser, name='active_user'),

    # url(r'^index/$',views.index),
]