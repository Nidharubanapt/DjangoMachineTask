
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('upload_task/', views.upload_task_completion, name='upload_task_completion'),
    path('available_pdfs/', views.available_pdfs, name='available_pdfs'),
     path('predict_marks/', views.predict_marks, name='predict_marks'),
    
]
