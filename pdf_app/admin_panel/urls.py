from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/upload/', views.upload_pdf, name='upload_pdf'),
    path('admin/update/<int:pk>/', views.update_pdf, name='update_pdf'),
    path('admin/delete/<int:pk>/', views.delete_pdf, name='delete_pdf'),
]
