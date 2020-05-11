from django.contrib import admin
from .models import *


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('tag',)
    # 每页记录数
    list_per_page = 10
    # 查询字段
    search_fields = ('tag',)


class ArticleAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('title', 'author', 'publishdate', 'det', 'pic','tag')
    fk_fields = ('tag',)
    # 每页记录数
    list_per_page = 10
    # 查询字段
    search_fields = ('title', 'author', 'publishdate', 'det', 'pic','tag')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags, TagAdmin)
