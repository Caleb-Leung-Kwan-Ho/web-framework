from turtle import title
from django.db import models

# Create your models here.
class Interest(models.Model):
    Hobby = models.CharField(max_length=100)
    slug = models.SlugField()
    rank = models.PositiveSmallIntegerField()    
    date = models.DateTimeField()


    def __str__(self):
        return self.Hobby


            