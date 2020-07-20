from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('tnc/', views.tnc, name='tnc'),
    path('comming-soon/', views.comming, name='comming'),
    path('contact/', views.contact, name='contact'), 
    path('merchantcontact/', views.merchantcontact, name='merchantcontact'),
]
