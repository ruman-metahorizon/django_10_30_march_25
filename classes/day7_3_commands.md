
## CRUD curl command:

`
Get all:
 curl --location 'http://localhost:8000/api/basic/'

Get one:
 curl --location 'http://localhost:8000/api/basic/1'

Create one:
    curl --location 'http://localhost:8000/api/basic/' \
--header 'Content-Type: application/json' \
--data '{   
        "first_name": "Ruman",  
        "last_name": "last_name",  
        "address": "Noida",  
        "roll_number": 105,  
        "mobile": "87975812"  
    }  '

Update one:
    curl --location --request PATCH 'http://localhost:8000/api/basic/1/update/' \
--header 'Content-Type: application/json' \
--data '{
    "first_name": "name_updated",
    "last_name": "last_name",
    "address": "Noida",
    "roll_number": 105,
    "mobile": "87975812"
}'

Delete one:
curl --location --request DELETE 'http://localhost:8000/api/basic/1/delete/'


`

## Postgresql


`

[Installation](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/)

python manage.py startapp movie

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',        # add this
    'movie',      # add this

]


`

## add movie/models.py

`
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.TextField()
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
`

## create movie/serializers.py

`
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        `

## update movie/views.py

`

from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

from rest_framework import status
from rest_framework.response import Response

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class AllMoviesListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    partial = True
    
    
class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))

`

## create movie/urls.py

`

from django.urls import path
from .views import MovieListCreateView, MovieDetailView,AllMoviesListView,MovieDeleteView,MovieUpdateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/all/', AllMoviesListView.as_view(), name='all-movies-list'),  
    path('movies/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'), 
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'), 
]
`

## update settings.py

`
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase', #change it databasename
        'USER': 'mydatabaseuser', #change it database user name
        'PASSWORD': 'mypassword', # change user database password
        'HOST': 'localhost',  
        'PORT': '5432',           
    }

`

## run command:

`

psql -U postgres


`