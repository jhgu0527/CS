from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NewsTag
from .serializers import NewsTagSerializer
from rest_framework import permissions


# Create your views here.
# @csrf_exempt
class NewsTagViewSet(viewsets.ModelViewSet):
    queryset = NewsTag.objects.all()
    serializer_class = NewsTagSerializer
    permission_classes = [permissions.AllowAny]


def index(request):
    return HttpResponse("index")
