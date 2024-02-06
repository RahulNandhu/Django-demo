from django.db import models

# Create your models here.

class Movies(models.Model):
    title=models.CharField(max_length=30)
    info=models.CharField(max_length=100)
    year=models.IntegerField()
    cover=models.ImageField(upload_to='movies', null=True,blank=True)

    def __str__(self):
        return self.title
