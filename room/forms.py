from django import forms
from django.forms import fields
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, MonthPickerInput

from room.models import Room
from users.models import Student

class CreateRoomForm(forms.Form):
    address = forms.CharField(label='Address', max_length=80)
    room_number = forms.CharField(label='Room number', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')
    is_insulated = forms.BooleanField(label='Is Insulated?', required=False)
    has_bathroom = forms.BooleanField(label='Has Bathroom?', required=False)
    student = forms.ModelChoiceField(Student.objects.all(), label='Student')

    
    
class UpdateRoomForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')

    class Meta:
        model = Room
        fields = ['address', 'square_meters', 'windows', 'is_insulated', 'has_bathroom']
        
        
class RegisterConsumptionForm(forms.Form):
    electricity = forms.IntegerField(label='Electricity (kWh)')
    gas = forms.IntegerField(label='Gas (kWh)')
    water = forms.IntegerField(label='Water (m^3)')
    date = forms.DateField(widget=MonthPickerInput())