from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def disease_page(request):
    return render(request, "disease/disease_home.html")

def predict_disease(request):
    if request.method == 'POST':
        # Dummy ML output (replace later)
        result = "Normal Eye"
        confidence = 0.87

        return render(request, 'disease/disease_result.html', {
            'result': result,
            'confidence': confidence
        })
    return render(request, "disease/disease_home.html")
