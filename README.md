# djangorestID

Mastering Django Rest Framework Tutorial Indonesia

## Django REST Framework Tutorial 3: Class-based Views

**Commands:**
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
* About APIView:\
https://www.django-rest-framework.org/api-guide/views/#class-based-views

* About Django CBV mixins:\ 
https://docs.djangoproject.com/en/4.0/topics/class-based-views/mixins/

* About DRF mixins:\
https://www.django-rest-framework.org/api-guide/generic-views/#mixins

* About GenericAPIView:\
https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview

**Refactoring of Our API views:**\
FBV (@api_view decorator) --> CBV (APIView class)  --> CBV (using DRF mixins)
