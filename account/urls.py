from django.urls import path
from . import views

urlpatterns = [
    path('', views.accthome, name='acct-home'),
]
