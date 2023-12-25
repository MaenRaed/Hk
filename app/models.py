from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    Name = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Number = models.IntegerField()
    Date = models.DateField()
    Time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    