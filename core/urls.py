from core.views import *
from django.urls import path


urlpatterns = [
    path("", home, name = "home"),
    path("shop/", shop, name ="shop"),
    path("news/", news, name = "news"),
    path("blog/", blog, name = "blog" ),
    path("login/", login, name="login"),
    path("about/", about, name = "about"),
    path("contact/",contanct, name = "contanct"),
    path("register/", register, name="register"),
    path("elements/", elements, name = "elements"),
    path("blog-details/", blogdetails, name = "blogdetails"),
    path("shop/<slug:slug>", productdetails, name = "productdetails"),
    
]








