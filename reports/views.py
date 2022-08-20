from django.db.models.aggregates import Count
from django.shortcuts import render
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from room.models import Consumption, Room
from users.models import *
from appliances.models import *
from django.db.models import Sum, fields
# Create your views here.

def main(request):
    return render(request, 'reports/reports.html')


class ListReport(SlickReportView):
    report_model = Consumption
    # the model containing the data we want to analyze
    date_field = 'date'
    # a date/datetime field on the report model
    # fields on the report model 
    columns = ['room_number_id', 'date', 'electricity', 'gas', 'water']


class TotalOfConsumption(SlickReportView):
    report_model = Consumption
    # the model containing the data we want to analyze
    date_field = 'date'
    group_by = 'room_number__room_number'
    # a date/datetime field on the report model
    # fields on the report model 
    columns = ['room_number__room_number',  SlickReportField.create(method=Sum, field='electricity', name='sum__electricity',verbose_name=('Total Electricity khW'))  ]
    
    chart_settings = [{
        'type': 'column',
        'data_source': ['sum__electricity'],
        'plot_total': False,
        'title_source': 'title',
        'title': ('Detailed Columns'),
        },
        {'type': 'pie',
         'data_source': ['sum__electricity'],
         'plot_total': False,
         'title_source': 'title',
         'title': ('Detailed Pie'),
         },
    ]



class LandlordReports(SlickReportView):
    report_model = Appliances
    date_field = 'date'
    group_by = 'room__room_number'
    columns = ['room__room_number',SlickReportField.create(method=Sum, field='actions', name='sum_date', verbose_name=('Quantity of Actions'))]

    chart_settings = [{
        'type': 'column',
        'data_source': ['sum_date'],
        'plot_total': False,
        'title_source': 'title',
        'title': ('Detailed Columns'),
        },
        {'type': 'pie',
         'data_source': ['sum_date'],
         'plot_total': False,
         'title_source': 'title',
         'title': ('Detailed Pie'),
         },
    ]