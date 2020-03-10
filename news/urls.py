from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'newstag', views.NewsTagViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'index/', views.index),
]