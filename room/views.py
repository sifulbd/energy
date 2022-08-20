from django.core.files.base import ContentFile
from django.shortcuts import render, redirect

from users.models import Landlord, Student
from appliances.models import *
from .models import Consumption, Room
from .forms import CreateRoomForm, UpdateRoomForm, RegisterConsumptionForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from appliances.forms import CreateActionForm

# Create your views here.


@login_required
def home(request):
    user = request.user
    if user.check_is_landlord():
        landlord = Landlord.objects.get(user_id = user.id)
        cuartos = Room.objects.all().filter(landlord_id = landlord.user_id)
        return render(request, 'room/rooms.html', {'cuartos': list(cuartos)})
    elif user.check_is_student():
        student = Student.objects.get(user_id = user.id)
        room = Room.objects.all().filter(student = student).first()
        appliances = Appliances.objects.all().filter(room = room)[0:5]
        actions = Actions.objects.all().filter(appliance_id__in=appliances.values_list('id'))[0:5]
        if actions == None:
            actions = list()
        return render(request, 'room/roomstudent.html', {'room': room, 'appliances': list(appliances), 'actions': list(actions)})
    else:
        return HttpResponse(200, user.check_is_student())
        


@login_required
def create(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            landlord = Landlord.objects.get(user_id = request.user.id)
            student = Student.objects.get(user_id = form.cleaned_data['student'])
            room = Room(
                room_number = form.cleaned_data['room_number'],
                address = form.cleaned_data['address'],
                square_meters = form.cleaned_data['square_meters'],
                windows = form.cleaned_data['windows'],
                is_insulated = form.cleaned_data['is_insulated'],
                has_bathroom = form.cleaned_data['has_bathroom'],
                landlord = landlord,
                student = student
            )
            room.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'room/createroom.html', {'form': form })
    else:
        form = CreateRoomForm()
        return render(request, 'room/createroom.html', {'form': form })
    
@login_required
def edit(request, id):
    if request.method == "POST":
        form = UpdateRoomForm(request.POST, instance=Room.objects.get(room_number=id))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'room/editroom.html', {'form': form })
    else:
        form = UpdateRoomForm(instance=Room.objects.get(room_number=id))
        return render(request, 'room/editroom.html', {'form': form })

@login_required
def register_consumption(request, room_number):
    if request.method == "POST":
        form = RegisterConsumptionForm(request.POST)
        if form.is_valid():
            consumption = Consumption(
                room_number=Room.objects.get(room_number=room_number),
                electricity=form.cleaned_data['electricity'],
                gas=form.cleaned_data['gas'],
                water=form.cleaned_data['water'],
                date=form.cleaned_data['date']
            )
            consumption.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'room/register_consumption.html', {'form': form , 'room_number':room_number})
    else:
        form = RegisterConsumptionForm()
        return render(request, 'room/register_consumption.html', {'form': form , 'room_number':room_number})
