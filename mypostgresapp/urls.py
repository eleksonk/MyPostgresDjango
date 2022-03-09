from django.urls import path
from . import views
urlpatterns=[
    path('index', views.index, name = 'index'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.login, name = 'login'),    
    path('vehicleAll', views.vehicleAll, name = 'vehicleAll'),
    path('vehicleUrl/<str:veh_no>', views.vehicleUrl, name = 'vehicleUrl'),    
    path('vehicleParticular', views.vehicleParticular, name = 'vehicleParticular'),        
    path('vehicleClassEntry', views.vehicleClassEntry, name = 'vehicleClassEntry'),     
    #for dropdownlist
    path('vehicleEntry', views.vehicleEntry, name = 'vehicleEntry'),
    #for action only
    path('saveVehicle', views.saveVehicle, name = 'saveVehicle'),
]