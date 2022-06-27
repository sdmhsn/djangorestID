# djangorestID

Mastering Django Rest Framework Tutorial Indonesia

## Django REST Framework Tutorial 4: Authentication & Permissions

**Commands:**
* Delete the database and start again:\
```rm -f db.sqlite3```  # Delete the database\
```rm -r snippets/migrations``` # Delete the migrations directory\
```python manage.py makemigrations snippets```\
```python manage.py migrate```\
```python manage.py createsuperuser```

* Testing our API using curl with verbose:\
```curl -v http://127.0.0.1:8000/snippets/```

* Testing format suffixes to our URLs using curl:\
```curl http://127.0.0.1:8000/snippets.json``` # JSON suffix\
```curl http://127.0.0.1:8000/snippets.api``` # Browsable API suffix

* Testing format suffixes with Accept header using curl"\
```curl -v -H "Accept:application/json" http://127.0.0.1:8000/snippets/```\
```curl -H "Accept:text/html" http://127.0.0.1:8000/snippets/```

* Testing POST request with curl:\
```curl -v -d code='print(123)' http://127.0.0.1:8000/snippets/``` # Content-Type: application x-www-form-urlencoded\
```curl -v -X POST -d "{\"code\": \"print(456)\"}" -H "Content-Type: application/json" http://127.0.0.1:8000/snippets/``` # Content-Type: application/json

**Resources:**
* About Authentication & Permissions:\
https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

* About ModelSerializer:\
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

* About ListAPIView:\
https://www.django-rest-framework.org/api-guide/generic-views/#listapiview

* About RetrieveAPIView:\
https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview

* About .perform_create():\
https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#associating-snippets-with-users\
https://www.django-rest-framework.org/api-guide/generic-views/#methods # (Save and deletion hooks)

* About ReadOnlyField:\
https://www.django-rest-framework.org/api-guide/fields/#readonlyfield\
https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#updating-our-serializer
