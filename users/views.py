from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from users.forms import RegisterForm, UpdateProfileForm, UpdateUserForm
from users.models import User, Profile
from django.contrib import messages
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from .models import *


def initial(request):
    return render(request, 'users/initial.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            is_landlord = 'is_landlord' == form.cleaned_data['radio_buttons']
            is_student = 'is_student' == form.cleaned_data['radio_buttons']
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                password= make_password(form.cleaned_data['password']),
                is_landlord = is_landlord,
                is_student = is_student,
            )
            user.save()
            if is_landlord == True:
                group = Group.objects.get(name='landlord')
                user.groups.add(group)
                landlord = Landlord(
                    user_id = user.id
                )
                landlord.save()
            if is_student == True:
                group = Group.objects.get(name='student')
                user.groups.add(group)
                student = Student(
                    user_id = user.id
                )
                student.save()
        return HttpResponseRedirect('/login')
    else:
        user_form = RegisterForm()
        return render(request, 'users/signup.html', {'form': user_form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('/profile/')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)  

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def login(request):
        return None


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('/profile/') 