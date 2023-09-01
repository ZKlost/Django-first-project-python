from django.shortcuts import render

# Create your views here.

def login(requests):
    return render(requests, "Login.html") 

def register(requests):
    return render(requests, 'Register.html')