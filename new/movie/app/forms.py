from django import forms

from .models import Movies

class Movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields="__all__"

