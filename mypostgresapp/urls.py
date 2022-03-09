from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name = 'index'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.login, name = 'login'),    
    path('vehicleAll', views.vehicleAll, name = 'vehicleAll'),
    path('vehicleUrl/<str:veh_no>', views.vehicleUrl, name = 'vehicleUrl'),    
    path('vehicleParticular', views.vehicleParticular, name = 'vehicleParticular'),        
    path('vehicleClassEntry', views.vehicleClassEntry, name = 'vehicleClassEntry'),     
    #First method of binding dropdownlist with db - 1
    path('vehicleEntry', views.vehicleEntry, name = 'vehicleEntry'),
    #for action only
    path('saveVehicle', views.saveVehicle, name = 'saveVehicle'),

    #another method of binding dropdownlist with db - 2
    path('entryForm', views.entryForm, name = 'entryForm'),
    path('entrySave', views.entrySave, name = 'entrySave'),
    
    path('base',views.base, name = 'base'),
    
]