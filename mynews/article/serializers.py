from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('__all__')


class ArticleDetailSerializers(serializers.ModelSerializer):
    tag = TagSerializer()
    publishdate = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Article
        fields = ('__all__')


class ArticleSerializers(serializers.ModelSerializer):
    tag = TagSerializer()
    publishdate = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Article
        fields = ('id','title', 'author', 'tag', 'pic','publishdate')
