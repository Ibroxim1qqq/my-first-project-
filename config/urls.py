from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news import views  # detail view uchun kerak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),  # ← bu yerda vergul qo‘shildi
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
