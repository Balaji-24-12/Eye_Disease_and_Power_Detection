from django.urls import path
from .views import disease_page
from .views import predict_disease

urlpatterns = [
    path('', disease_page, name='disease_page'),
    path('predict/',predict_disease,name='predict_disease')
]
