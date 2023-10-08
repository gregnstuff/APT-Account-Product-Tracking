from django.urls import path
from . import views

urlpatterns = [
    path('', views.issuehome, name='issue-home'),
]
