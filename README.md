# djangorestID

Mastering Django Rest Framework Tutorial Indonesia

## Django REST Framework Tutorial 2: Requests and Responses

**Commands:**
* Testing our API using curl with verbose:\
```curl -v http://127.0.0.1:8000/snippets/```

* Testing format suffixes to our URLs using curl:\
```curl http://127.0.0.1:8000/snippets.json``` # JSON suffix\
```curl http://127.0.0.1:8000/snippets.api``` # Browsable API suffix

* Testing format suffixes with Accept header using curl"\
```curl -v -H "Accept:application/json" http://127.0.0.1:8000/snippets/```\
```curl -H "Accept:text/html" http://127.0.0.1:8000/snippets/```