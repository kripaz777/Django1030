from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['categories'] = Category.objects.all()
    views['all_news'] = News.objects.all()
    views['featured_news'] = News.objects.filter(featured = True)
    views['popular_news'] = News.objects.filter(popular=True)
    views['latest_news'] = News.objects.filter(latest=True)
    views['sliders'] = News.objects.filter(slider=True)

    return render(request,'index.html',views)


def contact(request):

    return render(request,'contact.html')

def category(request,slug):
    views = {}
    cat_id = Category.objects.get(slug = slug).id
    views['cat_news'] = News.objects.filter(category_id=cat_id)
    return render(request,'category.html',views)

def single(request):

    return render(request,'single.html')