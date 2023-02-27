from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms
from .forms import ContactForm



def homepage(request):
    context = {'year': 2023}  # Replace 2023 with the current year
    return render(request, 'darkhome/homepage.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['your_email@example.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def album(request):
    return render(request, 'album.html')



