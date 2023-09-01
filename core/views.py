from django.shortcuts import render
from django.http import HttpResponse
from core.models import Setting, Product
# Create your views here.

def home(requests):
    products=Product.objects.all()
    context={
        "name" : "Django",
        "title" : "Home Page", 
        "products" : products[:4]
    }
    return render(requests, "index.html", context)


def shop(requests):
    context = {
        "name" : "Djnago",
        "title" : "Shop",
        "products" : Product.objects.all()
    }
    return render (requests, 'shop.html', context)

def about(requests):
    return render (requests, 'about.html')

def contanct(requests):
    return render (requests, 'contact.html')

def blog(requests):
    return render(requests, 'blog.html')

def blogdetails(requests):
    return render(requests, 'blog_details.html')

def elements(requests):
    return render(requests, 'elements.html')

def productdetails(requests, slug):
    context = {
        'products' : Product.objects.get(slug=slug),

    }
    return render(requests, 'product_details.html', context)

def news(requsets):
    return HttpResponse("hello")

def login(requests):
    return render(requests, "Login.html") 

def register(requests):
    return render(requests, 'Register.html')

