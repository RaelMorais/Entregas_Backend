import django_filters
from .models import Autor, Genero, Livros

class LivrosFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='')
    autor = django_filters.ModelChoiceFilter(queryset=Autor.objects.all(),label='')#Queryset é usado para selecionar o campo de escolha 
    genero = django_filters.ModelChoiceFilter(queryset=Genero.objects.all(), label='')
    ISBN = django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'genero', 'ISBN']

