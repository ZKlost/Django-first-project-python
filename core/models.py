from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

# Create your models here.
 
class Base_model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        abstract = True


class Setting(Base_model):
    logo = models.ImageField(upload_to="logo")
    phone1 = models.CharField(max_length=255)
    adress = models.CharField(max_length=300)
    email = models.EmailField()
    twiter = models.URLField()
    facebook = models.URLField()
    pinterest = models.URLField()


    class Meta:
        verbose_name = "Setting"
        verbose_name_plural= "Setting"

class Category(Base_model):
    title=models.CharField(max_length=255)


    def __str__(self):
        return self.title





class Category(Base_model):
    title=models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Category"


class Product(Base_model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    logo = models.ImageField(upload_to="products")
    price = models.CharField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.title
        return self.logo


class News(Base_model):
    title = models.CharField(max_length=255)
    content = models.CharField()
    image = models.ImageField(upload_to="news", null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models. IntegerField(default=0)
    views = models.IntegerField(default=0)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "News"
        verbose_name_plural= "News"
