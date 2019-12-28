from django import forms
from .models import inputmodel

class inputForm(forms.ModelForm):

    class Meta:
        model = inputmodel
        fields = '__all__'