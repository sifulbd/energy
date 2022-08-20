from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm
from .models import User, Profile, Student, Landlord

#class CustomUserAdmin(UserAdmin):
#    add_form = UserForm

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Landlord)