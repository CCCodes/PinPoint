from django.conf.urls import url
from django.urls import path, include

from homepage import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='homepage')
]
