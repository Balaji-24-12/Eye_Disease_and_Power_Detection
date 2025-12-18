from django.urls import path
from .views import predict_power
from .views import power_home

urlpatterns = [
    path('predict/', predict_power, name='predict_power'),
    path('', power_home, name='power_home'),
]
