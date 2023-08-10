from django import forms
from .models import File
from django.forms import ClearableFileInput

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["filepath"]
        widgets = {
            "filepath": ClearableFileInput(),
        }
