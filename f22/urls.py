from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.post_new, name='post_new'),
    url(r'^[a-z0-9A-Z]+$',views.post_redr,name='post_redr')
]
