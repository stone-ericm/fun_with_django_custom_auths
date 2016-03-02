from django import forms
from .models import Url
# these are already given to us 
from django.contrib.auth.models import User


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = [
            "actual",
        ]
