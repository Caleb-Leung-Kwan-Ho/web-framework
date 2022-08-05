from django.db import models

# Create your models here.
class certif_list(models.Model):
    name= models.CharField(max_length=100)
    rank = models.PositiveSmallIntegerField()
    confirment = models.URLField()

    def __str__(self):
        return self.name