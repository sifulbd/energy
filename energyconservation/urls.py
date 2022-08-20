"""energyconservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
import appliances
from users.views import ChangePasswordView
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views as user_views
from room import views as room_views
from appliances import views as appliances_views
from reports import views as report_views

urlpatterns = [
    path('',user_views.initial, name='initial'),
    #path('home/',room_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', user_views.signup, name= "signup"),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('room/home', room_views.home, name='home'),
    path('room/create/', room_views.create, name='create_room'),
    path('room/edit/<id>', room_views.edit, name='edit_room'),
    path('appliance/home', appliances_views.home, name='appliance'),
    path('room/register/consumption/<room_number>', room_views.register_consumption, name='register_consumption'),
    path('appliance/create/<room_number>', appliances_views.create, name='create_appliance'),
    #path('appliance/create/', appliances_views.createAppl, name='create_appliance_post'),
    path('appliance/edit/<id>', appliances_views.edit, name='edit_appliance'),
    path('appliance/create/action/<room_number>/<appliance_id>', appliances_views.create_action, name='create_action'),
    
    
    #Reports
    path('reports/', report_views.main, name='reports'),
    path('reports/listreport/', report_views.ListReport.as_view(), name='list_report'),
    path('reports/totalcomsuption/', report_views.TotalOfConsumption.as_view(), name='total_consumption'),
    path('reports/landlordreport/', report_views.LandlordReports.as_view(), name='landlord_report') 
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)