from django import forms
from .models import Task


class task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_desc',)
        widgets = {
            'task_desc': forms.TextInput(attrs={'class': 'Django_form_field',
                                                'placeholder':'Enter your task',
                                                }),
        }
        labels = {
            'task_desc':''

        }