from django.urls import path
from .views import predict_power

urlpatterns = [
    path('predict/', predict_power, name='predict_power'),
]
