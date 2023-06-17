from django.shortcuts import render
from my_app.models import *

def function(request):
    
    data = {


    }
    return render(request , 'index.html', data)

def uz_page(request):
    news = UzbekistanNews.objects.all()
    data = {
        "yangiliklar" : news
    }
    return render(request , 'uznews.html', data)

def gl_page(request):
    news = GlobalNews.objects.all()
    data = {
        "yangiliklar" : news
    }
    return render(request , 'glnews.html', data)

def sp_page(request):
    news = SportNews.objects.all()
    data = {
        "yangiliklar" : news
    }
    return render(request , 'spnews.html', data)


