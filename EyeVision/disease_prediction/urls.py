from django.urls import path
from .views import disease_page

urlpatterns = [
    path('', disease_page, name='disease_page'),
]
