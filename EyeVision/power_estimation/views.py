from django.shortcuts import render

def power_home(request):
    return render(request, "power/power_home.html")

def predict_power(request):
    if request.method == 'POST':
        # Dummy ML output
        left_eye = -1.75
        right_eye = -2.00

        return render(request, 'power/power_result.html', {
            'left_eye': left_eye,
            'right_eye': right_eye
        })
    return render(request, "power/power_home.html")

def power_page(request):
    return render(request, "power/power_home.html")