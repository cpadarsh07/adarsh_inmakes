from .models import Task
from django import forms

class ToDoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task','priority','date']

