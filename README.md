# TODO task manager

# Table of contents

- [Basic Information](#basic-information)
- [Guide in using TODO API](#guide-in-using-TODO-API)
- [API endpoints](#API-endpoints)

## Basic Information

TODO task manager is the task management

- URL Address: http://localhost:8001
- Technologies used :
  - Python v3.8.3
  - Django==3.0.8
  - PostgreSQL v12
  - python-decouple==3.3
  - djangorestframework-simplejwt==4.4.0
  - django-filter==2.3.0
- GitHub link for [Django](https://github.com/django/django)
- GitHub link for [DRF](https://github.com/encode/django-rest-framework)
- GitHub link for [python-decouple](https://pypi.org/project/python-decouple/)
- PyPI link for [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/)
- GitHub link for [django-filter](https://github.com/carltongibson/django-filter)

## Guide for using TODO API:

```
1) Create new .env file and configure it:
    SECRET_KEY = "Your secret Key"

    DEBUG = True     # only for development

    DB_ENGINE = django.db.backends.postgresql
    DB_NAME = todo
    DB_USER = todo_user
    DB_PASSWORD = todo_user123
    DB_HOST = 127.0.0.1
    DB_PORT = 5432

2) Activate virtualenv
3) pip install -r requirements.txt
4) Configure postgreSQL database
5) python manage.py migrate
6) python manage.py createsuperuser
7) python manage.py runserver 8001
8) Configure Postman:
    Import collection and environment:
      + TODO Manager.postman_collection.json
      + TODO Manager.postman_environment.json
```

## API endpoints:

```
admin/
api/v1/token/ [name='token_obtain_pair']
api/v1/token/refresh/ [name='token_refresh']
api/v1/token/verify/ [name='token_verify']
api/v1/token/ [name='token_obtain_pair']
api/v1/token/refresh/ [name='token_refresh']
api/v1/token/verify/ [name='token_verify']
api/v1/ ^users/$ [name='user-list']
api/v1/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
api/v1/ ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
api/v1/ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
api/v1/ ^category/$ [name='category-list']
api/v1/ ^category\.(?P<format>[a-z0-9]+)/?$ [name='category-list']
api/v1/ ^category/(?P<pk>[^/.]+)/$ [name='category-detail']
api/v1/ ^category/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='category-detail']
api/v1/ ^todo/$ [name='todo-list']
api/v1/ ^todo\.(?P<format>[a-z0-9]+)/?$ [name='todo-list']
api/v1/ ^todo/(?P<pk>[^/.]+)/$ [name='todo-detail']
api/v1/ ^todo/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='todo-detail']
api/v1/ todo/multiple-delete/ [name='todo_multiple_delete']
api/v1/ ^$ [name='api-root']
api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
```

**Development**  
[Ramesh Pradhan](mailto:ramesrest@gmail.com)
