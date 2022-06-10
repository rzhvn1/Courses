# Course API

Courses API is a simple API allowing consumers to view, create and delete courses.

## Getting Started

Follow the instructions and enjoy API!

### Prerequisites	

What things you need to install the software and how to install them. Install using pip

```
pip install django
pip install djangorestframework
pip install python-decouple
```

### Installing

Add 'rest_framework' to your INSTALLED_APPS setting.
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
### Running the migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Creating a superuser
```
python manage.py createsuperuser
```

### Running Development Server
```
python manage.py runserver
```

## Documentation

Check the documentation to see how it works ---> [Apiary](https://courseapi7.docs.apiary.io/#reference)

## Built With

* [Python](https://www.python.org) - is an interpreted high-level general-purpose programming language.
* [Postman](https://www.postman.com) - s an API platform for building and using APIs
* [Django](https://docs.djangoproject.com/en/4.0/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs used

## Authors

Erzhan Muratov


## Acknowledgments

* Адиль Дуйшеналиев
* Медет Мусаев
* Имамидинов Агахан