from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def predict_power(request):
    return JsonResponse({'message': 'Power estimation working'})