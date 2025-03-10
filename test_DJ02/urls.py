"""
URL configuration for test_DJ02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings  # Импортируем settings
from django.conf.urls.static import static  # Импортируем static
from test_app import views
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nic_1/', views.nic_1, name='nic_1'),
    path('alex_2/', views.alex_2, name='alex_2'),
    path('alex_3/', views.alex_3, name='alex_3'),
    path('nic_2/', views.nic_2, name='nic_2'),
    path('news/', include('news.urls'))

   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
