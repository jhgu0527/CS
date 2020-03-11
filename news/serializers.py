from rest_framework import serializers
from .models import NewsTag

class NewsTagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='NewsTagId')
    word = serializers.CharField(source='TagName')
    freq = serializers.IntegerField(source='TagFrequency')

    class Meta:
        model = NewsTag
        fields = ('id', 'word', 'freq')