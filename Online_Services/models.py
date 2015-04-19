from django.db import models


class Login(models.Model):
    UserName = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


class Register(models.Model):
    UID = models.IntegerField(max_length=5, unique=True)
    Login_Name = models.CharField(max_length=20)
    Password = models.CharField(max_length=10)
    Confirmpassword = models.CharField(max_length=10)
    Phonenumber = models.IntegerField(max_length=10, unique=True)
    Email_id = models.CharField(max_length=50, unique=True)
