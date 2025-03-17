from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Livros
from .forms import AutorForm, LivrosForm
from .filters import LivrosFilter

def livros_list(request):
    title = "Biblioteca do Dodo"
    return render(request, 'livros_list.html', {'title': title})


def autor_list(request):
    autor = Autor.objects.all()
    return render(request, 'autores.html', {'autor':autor})

def create_autor(request):
    print(create_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'autor_form.html', {'form': form}) #Caso não tenha nada no formulario, redireciona para ser preenchido
    
def update_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'autor_form.html', {'form': form})
    
def delete_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request, 'autor_delete.html', {'autor':autor})



def livro_list(request):
    title = 'dodo'
    livros = Livros.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})

def livro_create(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivrosForm()
    return render(request, 'livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivrosForm(instance=livro)
    print(form)
    return render(request, 'livro_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    return render(request, 'livro_delete.html', {'livro': livro})

def livros_filters(request):
    livros_filter = LivrosFilter(request.GET, queryset=Livros.objects.all())
    return render(request, 'livros_listados.html', {'livros_filter': livros_filter})