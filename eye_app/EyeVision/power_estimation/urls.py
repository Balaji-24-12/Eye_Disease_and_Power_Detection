from django.urls import path
from .views import estimate_power

urlpatterns = [
    path('estimate/', estimate_power, name='estimate_power'),
]
