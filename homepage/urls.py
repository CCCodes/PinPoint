from django.conf.urls import url
from django.urls import path, include

from homepage import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='homepage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/submit/$', views.contact_submit, name='contact_submit'),
    url(r'^contact/submit//?(?P<success>[-\w\d]+)/?$', views.contact_response, name='contact_response')
]
