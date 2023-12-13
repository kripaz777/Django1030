from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['categories'] = Category.objects.all()
    views['all__news'] = News.objects.all()
    views['featured_news'] = News.objects.filter(featured = True)
    views['popular_news'] = News.objects.filter(popular=True)
    views['latest_news'] = News.objects.filter(latest=True)
    views['sliders'] = News.objects.filter(slider=True)

    return render(request,'index.html',views)


def contact(request):

    return render(request,'contact.html')

def category(request):

    return render(request,'category.html')

def single(request):

    return render(request,'single.html')