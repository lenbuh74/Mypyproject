from django.db import models
from django.http import BadHeaderError
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth


def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['lenbuh74@mail.ru']
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'lenbuh74@mail.ru', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('http://127.0.0.1:8000/form/thanks')

    else:
        form = ContactForm()
    return render(reguest, "contact.html", {'form': form, 'username': auth.get_user(reguest).username})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})
