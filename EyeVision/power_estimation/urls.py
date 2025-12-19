from django.urls import path
from .views import predict_power_view

urlpatterns = [
    path('', predict_power_view, name='power_home'),
    
]
