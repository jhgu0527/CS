from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'newstag', views.NewsTagViewSet)



urlpatterns = [
    # path(r'api/', include(router.urls)),
    path(r'api/newstag', views.newsTag_list),
    path(r'api/news', views.news_list),
    path(r'index/', views.index),
]