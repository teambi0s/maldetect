from django import forms

from .models import MalUrl


class MalUrlForm(forms.ModelForm):
    class Meta:
        model = MalUrl
        exclude = []
