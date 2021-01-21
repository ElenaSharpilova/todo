from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=10)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)