from django.forms import ModelForm
from .models import Pessoal

class formulario(ModelForm):
    class Meta:
        model = Pessoal
        fields = ['first_name','last_name','age','salary','bio', 'photo']


