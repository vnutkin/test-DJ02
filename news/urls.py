

from django.urls import path
from django.conf import settings  # Импортируем settings
from django.conf.urls.static import static  # Импортируем static
from news import views
urlpatterns = [
    path('', views.home, name='news_home'),


   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
