

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserProfile, TaskCompletion
from .ml_model import predict
import matplotlib.pyplot as plt
import io
import urllib, base64
import joblib
import os
from django.conf import settings
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, TaskCompletion
from .forms import TaskCompletionForm
from django.contrib.auth.decorators import login_required
from admin_panel.models import PDFDocument
from django.middleware.csrf import get_token





# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('user_dashboard')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_portal/register.html', {'form': form})
    











    
def user_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None  

    completed_tasks = TaskCompletion.objects.filter(user=request.user)

    return render(request, 'user_portal/dashboard.html', {
        'user_profile': user_profile,
        'completed_tasks': completed_tasks
    })  
    
    
    
    
    
    
    
    
    
    
    
    
    

def upload_task_completion(request):
    if request.method == 'POST':
        form = TaskCompletionForm(request.POST, request.FILES)
        if form.is_valid():
            task_completion = form.save(commit=False)
            task_completion.user = request.user
            task_completion.save()
            
            pdf_document = task_completion.pdf_document

            # Update the user's total points
            user_profile = request.user.userprofile
            user_profile.total_points += pdf_document.points
            user_profile.save()

            return redirect('user_dashboard')
    else:
        form = TaskCompletionForm()
    return render(request, 'user_portal/upload_task_completion.html', {'form': form})














def available_pdfs(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'user_portal/available_pdfs.html', {'pdfs': pdfs})









# Load the trained model
model_path = os.path.join(settings.BASE_DIR, 'trained_model.pkl')
model = joblib.load(model_path)

def predict_marks(request):
    predicted_marks = None
    graph = None

    if request.method == 'POST':
        number_courses = float(request.POST.get('number_courses'))
        time_study = float(request.POST.get('time_study'))
        features = np.array([[number_courses, time_study]])
        predicted_marks = model.predict(features)[0]

        # Create a simple plot for visualization
        plt.figure()
        plt.scatter([number_courses], [predicted_marks], color='red')
        plt.xlabel('Number of Courses')
        plt.ylabel('Predicted Marks')
        plt.title('Predicted Marks based on Number of Courses')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graph = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

    return render(request, 'user_portal/predict_marks.html', {
        'predicted_marks': predicted_marks,
        'graph': graph
    })