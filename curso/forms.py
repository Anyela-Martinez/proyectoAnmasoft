from django.forms import ModelForm
from curso.models import Curso

class CursoForm(ModelForm):
    class Meta:
        model=Curso
        exclude=['estado', 'user', 'usuario']