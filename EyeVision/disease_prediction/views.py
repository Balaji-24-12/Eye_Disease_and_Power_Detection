from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def predict_disease(request):
    return JsonResponse({'message': 'Disease prediction working'})