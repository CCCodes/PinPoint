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
    texts = AboutText.objects.all()
    context = {
        'texts': texts,
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')
