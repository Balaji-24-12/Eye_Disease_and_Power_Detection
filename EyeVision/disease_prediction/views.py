# from django.shortcuts import render
# from django.http import JsonResponse

# # Create your views here.
# def disease_page(request):
#     return render(request, "disease/disease_home.html")

# def predict_disease(request):
#     if request.method == 'POST':
#         # Dummy ML output (replace later)
#         result = "Normal Eye"
#         confidence = 0.87

#         return render(request, 'disease/disease_result.html', {
#             'result': result,
#             'confidence': confidence
#         })
#     return render(request, "disease/disease_home.html")

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ml.predict import predict_disease

def disease_page(request):
    if request.method == "POST":
        image = request.FILES.get("eye_image")

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_path = fs.path(filename)

        disease, confidence = predict_disease(image_path)

        return render(request, "disease/disease_result.html", {
            "disease": disease,
            "confidence": confidence,
            "image_url": fs.url(filename)
        })

    return render(request, "disease/disease_home.html")
