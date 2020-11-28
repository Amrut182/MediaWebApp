from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)