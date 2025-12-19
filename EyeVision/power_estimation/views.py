from django.shortcuts import render
from .ml.predict import predict_power

def power_home(request):
    return render(request, "power/power_home.html")

def predict_power_view(request):
    if request.method == "POST":
        age = int(request.POST["age"])
        axial_length = float(request.POST["axial_length"])

        result = predict_power(age, axial_length)

        return render(request, "power/power_result.html", {
            "power": result
        })

    return render(request, "power/power_home.html")