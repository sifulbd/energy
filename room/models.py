from django.db import models
from django.db.models.fields import DecimalField
from django.forms.widgets import DateInput
from users.models import Landlord, Student
from datetime import date, datetime, time
from django.utils import timezone

# Model for room
class Room(models.Model):
    address = models.CharField(default='12345678', max_length=30)
    room_number = models.IntegerField(primary_key=True)
    square_meters = models.IntegerField()
    windows = models.IntegerField(null=True)
    is_insulated = models.BooleanField(default=False, null=True)
    has_bathroom = models.BooleanField(default=False, null=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return "Room: " + str(self.room_number)
    
class Consumption(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    electricity = models.IntegerField()
    gas = models.IntegerField()
    water = models.IntegerField()
    date = models.DateField(default=timezone.now())