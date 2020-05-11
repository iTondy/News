from django.db import models
import datetime


class Tags(models.Model):
    tag = models.CharField(max_length=30, verbose_name="标签")

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.CharField(max_length=30, verbose_name='作者',null=True,blank=True)
    tag = models.ForeignKey(Tags, verbose_name="标签",default='',null=True,blank=True)
    publishdate = models.DateTimeField(default=datetime.datetime.now(), verbose_name='发布日期')
    det = models.CharField(max_length=5000, verbose_name="文章内容")
    pic = models.ImageField(upload_to='uploads', verbose_name="图片")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "新闻文章"
        verbose_name_plural = verbose_name
