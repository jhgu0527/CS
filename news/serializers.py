from rest_framework import serializers
from .models import NewsTag, News


class NewsTagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='NewsTagId')
    word = serializers.CharField(source='TagName')
    freq = serializers.IntegerField(source='TagFrequency')

    class Meta:
        model = NewsTag
        fields = ('id', 'word', 'freq')


class NewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='NewsId')
    title = serializers.CharField(source='Title')
    url = serializers.URLField(source='URL')
    freq = serializers.IntegerField(source='ReadFrequency')
    created_date = serializers.DateField(source='Created_Date')

    class Meta:
        model = News
        fields = ('id', 'title', 'url', 'freq', 'created_date')