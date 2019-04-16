from django.conf.urls import url,include
from django.http import HttpResponse
from .views import getsquare,postnum,cal_list


urlpatterns = [
    url(r'^calc/(?p<_number>\d+)',getsquare),
    url(r'^post/',postnum),
    url(r'^list/(?p<number>\d+)',call_list)),
    
]
