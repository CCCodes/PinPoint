from django.shortcuts import render

from .models import *

# Create your views here.


def home(request):
    texts = HomeText.objects.all()
    context = {
        'texts': texts,
    }
    return render(request, 'main.html', context)


def about(request):
    context = {
        'main1': AboutText.objects.filter(position="main1"),
        'main2': AboutText.objects.filter(position="main2"),
        'col1': AboutText.objects.filter(position="col1"),
        'col2': AboutText.objects.filter(position="col2"),
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')
