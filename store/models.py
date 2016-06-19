from django.db import models
import json
from io import StringIO
from contextlib import redirect_stdout

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    shine = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    rarity = models.IntegerField(null=False)
    color = models.CharField(max_length=50)
    faces = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    path = models.CharField(max_length=100, blank=False, null=False)
    product = models.ForeignKey(Product, null=True, related_name='images')

    def __str__(self):
        return self.path

class Review(models.Model):
    stars = models.IntegerField(null=False)
    body = models.CharField(max_length=250, blank=True, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    createdOn = models.DateField('date published', null=False)
    product = models.ForeignKey(Product, null=True, related_name='reviews')

    def __str__(self):
        buf = StringIO()
        with redirect_stdout(buf):
            print(str(self.stars) + " - ")
            print(self.body + " Submitted by: " + self.author)
            print(" on " + str(self.createdOn))
        return buf.getvalue()








