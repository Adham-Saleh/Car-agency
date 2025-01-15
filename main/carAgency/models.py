from django.db import models
# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=200)
    model = models.IntegerField()
    # image =
    company = models.CharField(max_length=200)
    km = models.IntegerField()

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
