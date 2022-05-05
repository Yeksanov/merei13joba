from django import forms
from .models import *
class FormCreate(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'