from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class adult(models.Model):
    Auser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.CharField(blank=True, max_length=12)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class young(models.Model):
    Yuser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = PhoneNumberField(blank=True)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
