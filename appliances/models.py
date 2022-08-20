from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.db.models.fields.reverse_related import ManyToOneRel
from room.models import Room
from datetime import datetime, time
from django.utils import timezone

label_choices = (
    ("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),
    ("5", "E"),
    ("6", "F"),
    ("7", "G"),
)
appliance_choice = (
    ("1", "LCD TV"),
    ("2", "Computer"),
    ("3", "Laptop"),
    ("4", "Lamp"),
    ("5", "Electric heater"),
    ("6", "Air conditioner"),
    ("7", "Mini-fridge"),
    ("8", "Fan"),
    ("9", "Extension cord"),
    ("10", "Smartphone charger"),
)

action_choice = (
    ("1", "LCD TV"),
    ("2", "Computer"),
    ("3", "Laptop"),
    ("4", "Lamp"),
    ("5", "Electric heater"),
    ("6", "Air conditioner"),
    ("7", "Mini-fridge"),
    ("8", "Fan"),
    ("9", "Extension cord"),
    ("10", "Smartphone charger"),
)


class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type
        
class Appliances(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    appliance_name = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    label_class = models.CharField(max_length=1, choices=label_choices)
    energycomsuption = models.IntegerField() 
    date = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.appliance_name


class Action_Appliance(models.Model):
    name = models.CharField(max_length=150)
    type = ManyToManyField(Type)
    
    def __str__(self):
        return self.name
    
class Actions(models.Model):
    date = models.DateField(null=True)
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    action_appliance = models.ForeignKey(Action_Appliance, on_delete=models.CASCADE)