from django.urls import path
from django.conf.urls import url
from . import views
app_name ='summer'
urlpatterns = [
url(r'^index/$', views.index),
url(r'^show/(?P<good_id>[0-9]+)$', views.show, name='show'),
url(r'^in/$', views.add_new, name='add_new'),
url(r'^out/$', views.out_new, name='out_new'),
url(r'^record/$', views.record_query, name='record_query'),
url(r'^storage/$', views.storage_show, name='storage_show'),
url(r'^storage_add/$', views.storage_add, name='storage_add'),  #增加库存信息
]