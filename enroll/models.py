from django.db import models

class Data(models.Model):
    enrollmentNumber=models.TextField()
    name=models.CharField(max_length=100)
    email=models.TextField()
    Address=models.TextField()
    PhoneNumber=models.TextField()
    Class=models.IntegerField()
    Gender=models.TextField()
