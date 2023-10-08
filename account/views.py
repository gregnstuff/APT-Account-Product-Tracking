from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


def accthome(request):
    return render(request, 'account/accthome.html', {'title': 'acctHome'})
