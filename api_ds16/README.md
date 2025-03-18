# Api Docs

API created for backend programming class at Senai

# 💥 Let's Starter

To use this project, you need: 

![My Skills](https://skillicons.dev/icons?i=python,django,mysql,graphql)

Create a Venv:
```python
python -m venv _env 

````
For necessary libraries in cmd uses: 
````bash 
pip install -r requirements.txt

````
# Basics configs

```settings.py```

```python
INSTALLED_APPS = [
'.....',
'<app_name>', 
'rest_framework', 
'graphene_django',

]
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<db name>',
        'USER': '<db user>, 
        'PASSWORD' : '<db password>', 
        'HOST' : 'localhost', 
        'PORT':'3306', 
    }
}

```
```<project name>/urls.py``` to include yours Urls. 
```python

from django.urls import path, include
urlpatterns = [
    '...', 
    path('', include('<app_name>.urls')),

```
## Models 
The Car model represents a car and its associated properties in the database. 
This model is used to store essential details about a car such as its name, manufacturer, horsepower, category, number of doors, number of wheels, color, year of manufacture, and fuel type.

### Model Fields

The code model example: 

```python

class Car(models.Model):
    name_car = models.CharField(max_length=255)  
    name_factory = models.CharField(max_length=255)  
    horsepower = models.FloatField()  
    category = models.CharField(max_length=255)  
    qty_ports = models.PositiveIntegerField()  
    qty_roads = models.PositiveIntegerField()  
    color = models.CharField(max_length=255)  
    year = models.PositiveIntegerField()

    choice_fuel = (
        ('gs', 'Gasoline'),
        ('gnv', 'Compressed Natural Gas'),
        ('al', 'Ethanol'),
        ('ev', 'Electric'),
        ('ds', 'Diesel'),
        ('bd', 'Biodiesel'),
        ('bs', 'Biofuel'), 
    )
    fuel = models.CharField(max_length=9, choices=choice_fuel)

    def __str__(self): 
        return self.self.nome


```
# Functions 

- **Create** cars. 
- **Read** datas in DB.
- **Update** datas.
- **Delete** datas in BD. 

# HTTP *Methods*

1. GET

```bash 
     http://127.0.0.1:8000/api/
```
The GET method in the URL http://127.0.0.1:8000/api/ is responsible for listing all cars registered in the system.
When this URL is accessed, the API returns a set of objects that represent all cars stored in the database.

Example:

**Request**
```curl
    curl --location 'http://127.0.0.1:8000/api/'
```
**Response**
```json

[
    {
        "id": 1,
        "name_car": "Honda",
        "name_factory": "NSX",
        "horsepower": 280,
        "category": "Coupe",
        "qty_ports": 2,
        "qty_roads": 4,
        "color": "Grey",
        "year": 1992,
        "fuel": "gs"
    },
    {
        "....."
    },
]

```
























 To API in Postman, acess: https://documenter.getpostman.com/view/41755227/2sAYkDNgVy#intro
