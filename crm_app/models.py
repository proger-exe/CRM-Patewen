from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.TextField()
    password = models.TextField()

class Worker(models.Model):
    username = models.TextField()
    password = models.TextField()
    name = models.TextField()
    orders = models.JSONField()
    position = models.TextField()

class Sprint(models.Model):
    name = models.TextField()
    tasks = models.JSONField()

class Order(models.Model):
    slug = models.SlugField()
    title = models.TextField()
    amount = models.IntegerField()
    client = models.IntegerField()

