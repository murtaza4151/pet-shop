from django import forms
from .models import order
class orderforms(forms.ModelForm):
    class Meta:
        model=order
        fields="__all__"