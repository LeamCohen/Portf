from .forms import ContactForm
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail

def index(response):
    return render(response,"app/index.html", {})

def success(response):
    return render(response,"app/success.html", {})