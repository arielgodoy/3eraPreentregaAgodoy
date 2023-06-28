from django.forms import ModelForm
from .models import Documento

class DocForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'