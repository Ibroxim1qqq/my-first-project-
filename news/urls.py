from django.urls import path
from news.views import news_list

urlpatterns = [
    path('', news_list)
]
