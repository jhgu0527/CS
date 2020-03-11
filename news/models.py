from django.db import models


# Create your models here.

class News(models.Model):
    NewsId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    body = models.TextField()
    ReadFrequency = models.IntegerField()


class NewsTag(models.Model):
    NewsTagId = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=100)
    TagFrequency = models.IntegerField()

    # class Meta:
    #     ordering = ['-TagFrequency']

    def __str__(self):
        return self.TagName
