from smtplib import SMTPAuthenticationError

from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

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


def contact_submit(request):
    try:
        send_mail(
            'PinPoint Site Contact from ' + request.POST['email'],
            'Name: ' + request.POST['name'] + '\nEmail: ' +
            request.POST['email'] + '\nMessage: ' + request.POST['message'],
            'proconduck@gmail.com',
            ['caitlinchou@gmail.com'],
            fail_silently=False
        )
    except SMTPAuthenticationError as e:
        print(e)
        return HttpResponseRedirect(reverse('home:contact_response', kwargs={
            'success': 'false'}))
    return HttpResponseRedirect(reverse('home:contact_response', kwargs={'success': 'true'}))


def contact_response(request, success):
    if success == 'true':
        message = "We have successfully sent your message. We will get back to you soon!"
        header_main = "Congratulations"
    elif success == 'false':
        message = "Sorry, something went wrong with sending your message."
        header_main = "We Are Sorry"
    else:
        raise Http404
    context = {
        'message': message,
        'header_main': header_main
    }
    return render(request, 'contact.html', context)
