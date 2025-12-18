from django.shortcuts import render

def predict_power(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        blur = int(request.POST.get("blur"))

        # dummy logic (ML comes later)
        power = round(blur * 0.25, 2)

        return render(request, "power_result.html", {
            "age": age,
            "power": power
        })

    return render(request, "power_result.html")
