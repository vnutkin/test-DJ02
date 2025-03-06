# Create your views here.
from django.shortcuts import render
from .models import News_post


def home(request):
	news = News_post.objects.all()
	data = {'main': 'yes', 'news':news}
	return render(request, 'news/news.html', data)
