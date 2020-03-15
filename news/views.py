from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
from .models import NewsTag, News
from .serializers import NewsTagSerializer, NewsSerializer
from rest_framework import permissions


@api_view(['GET', ])
def newsTag_list(request):
    """
    list all news hot topic key words
    :param request:
    :return:
    """
    if request.method == 'GET':
        newstag = NewsTag.objects.all()
        # TODO: many = True is important for objects.all
        serializers = NewsTagSerializer(newstag, many=True)
        return Response(serializers.data)

@api_view(['GET', ])
def news_list(request):
    """
    list all news
    :param request:
    :return:
    """
    if request.method == 'GET':
        news = News.objects.all()
        # TODO: many = True is important for objects.all
        serializers = NewsSerializer(news, many=True)
        return Response(serializers.data)

# Create your views here.

# class NewsTagViewSet(viewsets.ModelViewSet):
#     queryset = NewsTag.objects.all()
#     serializer_class = NewsTagSerializer
#     permission_classes = [permissions.AllowAny]

def index(request):
    return HttpResponse("index")
