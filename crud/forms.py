from django import forms
from django.forms import ModelForm
from .models import Documento



class DocForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'

class BuscaDocs(forms.Form):
    titulo = forms.CharField(max_length=100,required=False)