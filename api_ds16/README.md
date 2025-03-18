# Api Docs

API created for backend programming class at Senai

# 💥 Let's Starter

To use this project, you need: 

![My Skills](https://skillicons.dev/icons?i=python,django,mysql,graphql)
````bash 
python 3.9+

pip install djangorestframework

pip install mysqlclient

pip install graphql




````





















** Code ** 

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
