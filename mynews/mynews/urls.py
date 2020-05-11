"""mynews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import include, url
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from article.views import ArticleViewSet

from .settings import MEDIA_ROOT
router = DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url('^docs/', include_docs_urls(title='文章')),
    url(r'^', include(router.urls)),
    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
