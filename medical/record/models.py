from django.db import models
from datetime import datetime

#create your model here.
class Person(models.Model):
    name=models.CharField(max_length=300)
    age=models.IntegerField(default=0)
    bloodGroup=models.CharField(max_length=20)
    gender=models.CharField(max_length=30)

    def __str__(self):
        return self.Person
class MedicalRecord(models.Model):
    symptoms=models.CharField(max_length=300)
    medicines=models.CharField(max_length=300)
    membername=models.CharField(max_length=20)




    def __str__(self):
        return self.MedicalRecord





