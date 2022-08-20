from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Type)
admin.site.register(Appliances)
admin.site.register(Actions)
admin.site.register(Action_Appliance)
