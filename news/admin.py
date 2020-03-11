from django.contrib import admin
from .models import News, NewsTag
# Register your models here.

admin.site.register(News)
admin.site.register(NewsTag)