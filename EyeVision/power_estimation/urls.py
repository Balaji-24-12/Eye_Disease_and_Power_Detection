from django.urls import path
from .views import predict_power
from .views import power_page

urlpatterns = [
    path('', power_page, name='power_page'),
    path('predict/', predict_power, name='predict_power'),
    
]
