from django.urls import path
from .views import predict_disease
from .views import disease_home

urlpatterns = [
    path('', disease_home, name='disease_home'),
    
    
]
