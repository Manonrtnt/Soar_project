from django import forms
from .models import CaptureRequest

# Django form depending on model CaptureRequest
class CaptureRequestForm(forms.ModelForm):
    class Meta:
        model = CaptureRequest
        fields = ['requestName', 'requestUser', 'requestCode']