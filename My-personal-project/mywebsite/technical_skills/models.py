from turtle import title
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Technical_skills(models.Model):
    title = models.CharField(max_length=100)
    level = models.IntegerField(validators=[MaxValueValidator(2), MinValueValidator(0)])

    def __str__(self):
        return self.title

    def show(self):
        if (self.level==2):
            return "Strong"
        elif(self.level==1):
            return "intermediate"
        else:
            return "beginner"
            