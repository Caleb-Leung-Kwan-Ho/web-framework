from django.db import models

# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date= models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.title

class CCVV(models.Model):
    title = models.CharField(max_length=100)
    company_name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date= models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.title