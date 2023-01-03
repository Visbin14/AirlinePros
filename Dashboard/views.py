from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView,View,ListView
from django.views import generic
from Dashboard.forms import Dashboardform
from Dashboard.models import DashboardModel
from django.conf import settings
import datetime
import time
from django.core.files.storage import FileSystemStorage
import os
from django.urls import reverse_lazy
import pandas as pd
from django.template.loader import render_to_string
import json
import datetime
from django.core import serializers
from django.http import JsonResponse

class Dashboard(View):
    def get(self, request):
        is_filter = request.GET.get("is_filter")
        
        if is_filter:
            region = request.GET.get('region')
            country = request.GET.get('country')
            year = request.GET.get('year')
            airline = request.GET.get('airline')
            airline_IATA_code = request.GET.get('airline_IATA_code')
            IATA_numeric_code = request.GET.get('IATA_numeric_code')
            agreement_type = request.GET.get('agreement_type')
            contraced_with = request.GET.get('contraced_with')
            month = request.GET.get('month')
            orc_rate = request.GET.get("orc_rate")
            gross = request.GET.get("gross")
            nett = request.GET.get("nett")
            orc_actual = request.GET.get("orc_actual")
            
            response = {}
            source_data = DashboardModel.objects.all()
            if region:
                source_data =  source_data.filter(Region=region)
            if country:
                source_data = source_data.filter(Country=country)
            if year:
                source_data = source_data.filter(Year=year)
            if airline:
                source_data = source_data.filter(Airline=airline) 
            if airline_IATA_code:
                source_data = source_data.filter(Airline_IATA_Code=airline_IATA_code)
            if IATA_numeric_code:
                source_data = source_data.filter(IATA_Numeric_Code=IATA_numeric_code)
            if agreement_type:
                source_data = source_data.filter(Agreement_Type=agreement_type)
            if contraced_with:
                source_data = source_data.filter(Contraced_With=contraced_with)
            if month:
                source_data = source_data.filter(Month=month)
            if orc_rate:
                source_data = source_data.objects.filter(ORC_Rate=orc_rate)
            if gross:
                source_data = source_data.filter(Gross=gross)
            if nett:
                source_data = source_data.filter(Nett=nett)
            if orc_actual:
                source_data = source_data.filter(ORC_Actual=orc_actual)

            data = source_data
            output = render_to_string('dashboard_table.html',{'data':data})
            response['status'] = True
            response['html_to_replace'] = output
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        
        
        template_name = 'dashboard.html'
        
        
        
        data = DashboardModel.objects.all()
        unique_regions = DashboardModel.objects.all().values_list('Region', flat=True).distinct().order_by('Region')
        unique_country = DashboardModel.objects.all().values_list('Country', flat=True).distinct().order_by('Country')
        unique_year = DashboardModel.objects.all().values_list('Year', flat=True).distinct().order_by('Year')
        unique_airline = DashboardModel.objects.all().values_list('Airline', flat=True).distinct().order_by('Airline')
        unique_airline_IATA_code = DashboardModel.objects.all().values_list('Airline_IATA_Code', flat=True).distinct().order_by('Airline_IATA_Code')
        unique_IATA_numeric_code = DashboardModel.objects.all().values_list('IATA_Numeric_Code', flat=True).distinct().order_by('IATA_Numeric_Code')
        unique_agreement_type = DashboardModel.objects.all().values_list('Agreement_Type', flat=True).distinct().order_by('Agreement_Type')
        unique_contraced_with = DashboardModel.objects.all().values_list('Contraced_With', flat=True).distinct().order_by('Contraced_With') 
        unique_orc_rate = DashboardModel.objects.all().values_list('ORC_Rate', flat=True).distinct().order_by('ORC_Rate')
        unique_gross = DashboardModel.objects.all().values_list('Gross', flat=True).distinct().order_by('Gross')
        unique_nett = DashboardModel.objects.all().values_list('Nett', flat=True).distinct().order_by('Nett')
        unique_orc_actual = DashboardModel.objects.all().values_list('ORC_Actual', flat=True).distinct().order_by('ORC_Actual')
        
 
        
        
        
        return render(request, template_name,{'data':data,'unique_regions':unique_regions,'unique_country':unique_country,
                                              'unique_year':unique_year,'unique_airline':unique_airline,'unique_airline_IATA_code':unique_airline_IATA_code,
                                              'unique_IATA_numeric_code':unique_IATA_numeric_code,'unique_agreement_type':unique_agreement_type,
                                              'unique_contraced_with':unique_contraced_with,'unique_orc_rate':unique_orc_rate,
                                              'unique_gross':unique_gross,'unique_nett':unique_nett,'unique_orc_actual':unique_orc_actual})
        
class Uploaddashboardfile(FormView):

    template_name = 'dashboard-file-upload.html'
    form_class = Dashboardform
    # success_url = 'Airlinedashboard/'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        
        file = self.request.FILES['file']
        file_r = self.request.FILES['file'].read()
        file_name, extention = file.name.split('.')
        media_root = getattr(settings, 'MEDIA_ROOT')
        if extention.lower() == 'xlsx':
            errfiles = []
            errMsg = ''
            zipfileCnt = 0

            media_root = getattr(settings, 'MEDIA_ROOT')
            fs = FileSystemStorage(location=os.path.join(media_root, "Dashboard files/"))
            filename = fs.save(file_name + '.' + extention, file)
            dataframe = pd.read_excel(file,"DATABASE")
            for i in range(len(dataframe)):
                region = dataframe.loc[i].REGION
                country = dataframe.loc[i].COUNTRY
                year = dataframe.loc[i].YEAR
                airline = dataframe.loc[i].AIRLINE
                airline_iata_code = dataframe.loc[i]["AIRLINE IATA CODE"]               
                iata_numeric_code = dataframe.loc[i]["IATA NUMERIC CODE"]
                agreement_type = dataframe.loc[i]["AGREEMENT TYPE"]
                contracted_with = dataframe.loc[i]["CONTRACED WITH"]
                month = dataframe.loc[i].MONTH
                orc_rate = dataframe.loc[i].ORC_RATE        
                gross = dataframe.loc[i].GROSS
                nett = dataframe.loc[i].NETT
                orc_actual = dataframe.loc[i]["ORC ACTUAL"]
              
                
                create =  DashboardModel.objects.get_or_create(Region=region,Country=country,Year=year,Airline=airline,Airline_IATA_Code=airline_iata_code,
                                                               IATA_Numeric_Code=iata_numeric_code,Agreement_Type=agreement_type,Contraced_With=contracted_with,
                                                               Month=month,ORC_Rate=orc_rate,Gross=gross,Nett=nett,ORC_Actual=orc_actual
                                                               )   

          
            text_file = os.path.join(media_root, "Dashboard files/" + filename)
        
        return super(Uploaddashboardfile, self).form_valid(form)
       
    def form_invalid(self, form):
        print("<===============FORM INVALID========================>",form.errors)
        
        
class Pivot(View):
    def get(self,request):
        pd.set_option('display.float_format', '{:.2f}'.format)
        df = pd.DataFrame(list(DashboardModel.objects.all().values()))
        is_filter = request.GET.get("is_filter")
        if is_filter:
            orc_rate = request.GET.get("orc_rate")
            nett = request.GET.get("nett")
            country = request.GET.get('country')
            airline = request.GET.get('airline')
            IATA_numeric_code = request.GET.get('IATA_numeric_code')
            agreement_type = request.GET.get('agreement_type')
            gross = request.GET.get("gross")
            orc_actual = request.GET.get("orc_actual")
            nett = request.GET.get("nett")
            month = request.GET.get('month')
        
            response = {}
        
            source_data = DashboardModel.objects.all()    
            if month:
                source_data = source_data.filter(Month=month)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Month= month).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html() 
            if orc_rate:
                source_data = source_data.filter(ORC_Rate=orc_rate)
                df = pd.DataFrame(list(DashboardModel.objects.filter(ORC_Rate= orc_rate).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if nett:
                source_data = source_data.filter(Nett= nett)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Nett= nett).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if country:    
                source_data = source_data.filter(Country= country)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Country= country).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()
               

            if airline:
                source_data = source_data.filter(Airline= airline)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Airline= airline).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if IATA_numeric_code:
                source_data = source_data.filter(IATA_Numeric_Code= IATA_numeric_code)
                df = pd.DataFrame(list(DashboardModel.objects.filter(IATA_Numeric_Code= IATA_numeric_code).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if agreement_type:
                source_data = source_data.filter(Agreement_Type= agreement_type)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Agreement_Type= agreement_type).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if gross:
                source_data = source_data.filter(Gross= gross)
                df = pd.DataFrame(list(DashboardModel.objects.filter(Gross= gross).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            if orc_actual:
                source_data = source_data.filter(ORC_Actual= orc_actual)
                df = pd.DataFrame(list(DashboardModel.objects.filter(ORC_Actual= orc_actual).values()))
                pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
                pivot_data = pivot_data.to_html()

            
            output = render_to_string('pivot_table.html',{'pivot_data':pivot_data,'source_data':source_data})
            
            response['status'] = True
            response['html_to_replace'] = output
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        pivot_data = df.pivot_table( index="Month",columns="Year",values=["Gross","Nett"],aggfunc="sum",margins=True)
        pivot_data = pivot_data.to_html()
        unique_country = DashboardModel.objects.all().values_list('Country', flat=True).distinct().order_by('Country')
        unique_airline = DashboardModel.objects.all().values_list('Airline', flat=True).distinct().order_by('Airline')
        unique_IATA_numeric_code = DashboardModel.objects.all().values_list('IATA_Numeric_Code', flat=True).distinct().order_by('IATA_Numeric_Code')
        unique_agreement_type = DashboardModel.objects.all().values_list('Agreement_Type', flat=True).distinct().order_by('Agreement_Type')
        unique_orc_rate = DashboardModel.objects.all().values_list('ORC_Rate', flat=True).distinct().order_by('ORC_Rate')
        unique_gross = DashboardModel.objects.all().values_list('Gross', flat=True).distinct().order_by('Gross')
        unique_nett = DashboardModel.objects.all().values_list('Nett', flat=True).distinct().order_by('Nett')
        unique_orc_actual = DashboardModel.objects.all().values_list('ORC_Actual', flat=True).distinct().order_by('ORC_Actual')
        unique_month = DashboardModel.objects.all().values_list('Month',flat=True).distinct()
        
        return render(request, 'pivot.html',{'pivot_data':pivot_data,'unique_country':unique_country,'unique_airline':unique_airline,'unique_IATA_numeric_code':unique_IATA_numeric_code,
                                            'unique_agreement_type':unique_agreement_type,'unique_orc_rate':unique_orc_rate,'unique_gross':unique_gross,'unique_nett':unique_nett,
                                            'unique_orc_actual':unique_orc_actual,'unique_month':unique_month})    
         
    