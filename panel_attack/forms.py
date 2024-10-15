from django import forms
from .models import Panel

class panelForm(forms.Form):
    panel_id = forms.CharField(label="panel_id",
                               max_length=2)

    color = forms.CharField(label="color",max_length=100)
    answer = forms.CharField(label="answer",max_length=1000)
