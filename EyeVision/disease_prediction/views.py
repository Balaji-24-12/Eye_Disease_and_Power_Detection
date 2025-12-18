from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def predict_disease(request):
    return render(request, 'disease/disease_prediction.html')

def disease_home(request):
    return render(request, 'disease/disease_home.html')


def disease_page(request):
    if request.method == "POST":
        return render(request, "disease.html", {
            "result": "No disease detected (dummy output)"
        })
    return render(request, "disease/disease_home.html")
