from django import forms
from .models import Autor, Genero, Livros 

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome_autor', 'data_nascimento', 'descricao']


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['genero']

class LivrosForm(forms.ModelForm):
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=True)
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), required=True)
    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'genero','preco', 'resumo', 'ISBN']

        