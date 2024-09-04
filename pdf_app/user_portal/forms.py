
from django import forms
from .models import TaskCompletion

class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = TaskCompletion
        fields = ['pdf_document', 'screenshot']
