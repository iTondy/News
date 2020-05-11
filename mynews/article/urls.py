from django.conf.urls import url
from article import views


urlpatterns = [
     url(r'index', views.index),
     url(r'detail', views.detail),
]
