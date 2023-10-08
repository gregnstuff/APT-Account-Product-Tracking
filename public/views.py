from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'public/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'public/about.html', {'title': 'About'})
