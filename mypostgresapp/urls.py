from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name = 'index'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.login, name = 'login'),
    path('vehicleEntry', views.vehicleEntry, name = 'vehicleEntry'),
    path('vehicleAll', views.vehicleAll, name = 'vehicleAll'),
    path('vehicleUrl/<str:veh_no>', views.vehicleUrl, name = 'vehicleUrl'),
    path('vehicleParticular', views.vehicleParticular, name = 'vehicleParticular'),
]