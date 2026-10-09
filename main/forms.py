from django import forms
from .models import Animal, Desaparecido, Adocao

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'idade', 'especie', 'raca', 'porte', 'sexo', 'descricao_animal']

class DesaparecidoForm(forms.ModelForm):
    class Meta:
        model = Desaparecido
        fields = ['animal', 'contato', 'data_desaparecimento', 'descricao_desaparecido']

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['animal', 'data_publicacao', 'descricao_animal']
