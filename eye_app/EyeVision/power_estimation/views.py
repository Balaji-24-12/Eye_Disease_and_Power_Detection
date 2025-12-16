import joblib
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

model = joblib.load("power_estimation/model/power_model.pkl")

@csrf_exempt
def estimate_power(request):
    if request.method == 'POST':
        try:
            # Extract inputs
            AL  = float(request.POST.get("axial_length"))
            K1  = float(request.POST.get("k1"))
            K2  = float(request.POST.get("k2"))
            ACD = float(request.POST.get("acd"))
            LT  = float(request.POST.get("lens_thickness"))
            PD  = float(request.POST.get("pupil_diameter"))
            Age = int(request.POST.get("age"))

            features = np.array([[AL, K1, K2, ACD, LT, PD, Age]])
            power_value = model.predict(features)[0]

            return JsonResponse({
                'predicted_power': round(float(power_value), 2)
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'POST only'}, status=400)
