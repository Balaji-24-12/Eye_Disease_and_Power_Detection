import tensorflow as tf
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

model = tf.keras.models.load_model("disease_prediction/model/disease_model.h5")

@csrf_exempt
def predict_disease(request):
    if request.method == 'POST':
        image = request.FILES.get('eye_image')
        if not image:
            return JsonResponse({'error': 'Image missing'}, status=400)

        # Load & preprocess image
        img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Predict
        preds = model.predict(img_array)[0]
        classes = ["Normal", "Cataract", "Glaucoma", "Diabetic Retinopathy"]

        result = classes[np.argmax(preds)]

        return JsonResponse({
            'prediction': result,
            'confidence': float(np.max(preds))
        })

    return JsonResponse({'error': 'POST only'}, status=400)
