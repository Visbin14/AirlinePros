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
class Dashboard(View):
    def get(self, request):
        
        region = request.GET.get('region')
        print(region,"///////////////////////////////")
        if region:
            try:
                response = {}
                data =  DashboardModel.objects.filter(Region=region)
                output = render_to_string('dashboard_table.html',{'data':data})
                print(output,"///////////"
                )

                response['status'] = True
                response['html_to_replace'] = output
            except:
                response['status'] = False

           
        return HttpResponse(json.dumps(response), content_type="application/json")
        template_name = 'dashboard.html'
        # model = DashboardModel
            
        # def get_context_data(self, **kwargs):
        #     context = super(Dashboard, self).get_context_data(**kwargs)
        data = DashboardModel.objects.all()
        unique_regions = DashboardModel.objects.all().values_list('Region', flat=True).distinct()
        print(unique_regions,"/////////////////")
        # for i in unique_regions:
        #     print(i.Region,"////////////")
        
        
        
        #     # Asia = DashboardModel.objects.filter(Region="ASIA")
        #     # for asi in Asia:
        #     #     print(asi.Region)
        #     context["data"] = data
        return render(request, template_name,{'data':data,'unique_regions':unique_regions})
        
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