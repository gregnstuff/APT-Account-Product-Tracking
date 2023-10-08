from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


def issuehome(request):
    return render(request, 'issue/issuehome.html', {'title': 'issueHome'})
