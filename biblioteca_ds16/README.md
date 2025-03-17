<h1>A simple CRUD of Library</h1>

<p>This is an example CRUD repository for studies at Senai's in the Backend class on day 11/03</p>

## 🚀 Getting Started

🐍 Prerequisites
- Python 3.10.x or more
- Django
  
To install depedencies use:

```bash
pip install -r requirements.txt
```

## ⚡ Run the Project

```bash 
python manage.py runserver
```

After running the server, visit http://127.0.0.1:8000 in your browser to interact with the Library CRUD application.

## 🧑‍💻 Filtering Books with Django Filters

In this project, we're using ```django-filters``` to implement a filtering system for books (Livros) based on various fields like title, author, genre, and ISBN. Here's a breakdown of how the filter works.

- **Title (`titulo`)**: Filters books by partial, case-insensitive title matches.
- **Author (`autor`)**: Allows filtering by the book's author from a list of authors.
- **Genre (`genero`)**: Filters books based on their genre from a list of genres.
- **ISBN**: Filters books by partial, case-insensitive ISBN matches.

The filter is linked to the Livros model, allowing efficient searching in views. 
**Example**

````python
def livros_filters(request):
    livros_filter = LivrosFilter(request.GET, queryset=Livros.objects.all())
    return render(request, 'livros_listados.html', {'livros_filter': livros_filter})
````

To develop this project I used

![My Skills](https://skillicons.dev/icons?i=django,html,tailwind,bootstrap,python,sqlite)
