from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.fields.related import OneToOneField
from django.forms import widgets
from django import forms
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create models here.
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(default='12345678', max_length=30)
    is_landlord = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
        
    def check_is_landlord(self):
        if self.is_landlord:
            return True
        return False
    def check_is_student(self):
        if self.is_student:
            return True
        return False

    def __str__(self):
        return self.first_name + self.last_name
        
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.first_name +" "+ self.user.last_name
    
    
class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username