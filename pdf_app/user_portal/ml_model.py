import joblib
import os
from django.conf import settings

# Load the trained model
model_path = os.path.join(settings.BASE_DIR, 'trained_model.pkl')
model = joblib.load(model_path)

def predict(number_courses, time_study):
    features = [[number_courses, time_study]]
    predicted_marks = model.predict(features)[0]
    return predicted_marks
