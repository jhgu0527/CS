from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
from .models import NewsTag
from .serializers import NewsTagSerializer
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
        serializers = NewsTagSerializer(newstag)
        return Response(serializers.data)

# Create your views here.
# @csrf_exempt
# class NewsTagViewSet(viewsets.ModelViewSet):
#     queryset = NewsTag.objects.all()
#     serializer_class = NewsTagSerializer
#     permission_classes = [permissions.AllowAny]

def index(request):
    return HttpResponse("index")
