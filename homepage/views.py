from django.shortcuts import render

# Create your views here.


def home(request):
    fields = {}
    return render(request, 'main.html')
