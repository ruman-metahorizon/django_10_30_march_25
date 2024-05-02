Introduction
Project Overview:
Imagine you want to build a digital to-do list, where you can create, update, and complete tasks. This project is like that, but it’s a bit more sophisticated. We’re going to create a Task Management API using Django Rest Framework (DRF) and store the tasks in a PostgreSQL database.

Purpose:
The main reason we’re doing this is to learn how to build an API with Django. APIs are like bridges that allow different software applications to communicate. By the end of this project, you’ll have a good understanding of how to create APIs, and you’ll have a working example to show off!

Scope:
We’re going to cover a lot of ground, but we won’t make things too complicated. We’ll create an API that can create, read, update, and delete tasks. While this might not seem like much, it’s a solid foundation for more complex projects.

Environment Setup
Python Installation:

To get started, you’ll need Python. Think of Python as the language we’ll use to tell our computer what to do. You can download it from the [Python website](https://www.python.org/downloads/).

Virtual Environment:
1)It’s a good idea to create a virtual space for your project. Think of it as a little playground where your project’s dependencies won’t mess with other things on your computer.
2)To do this, open your computer’s terminal (or command prompt on Windows) and run the following commands:
On macOS and Linux:

python3 -m venv myenv
source myenv/bin/activate

On Windows:

python -m venv myenv
myenv\Scripts\activate

Djnago Install
we will install Django and set up our Django app inside the virtual environment.

pip install django djangorestframework

PostgreSQL Installation:
This is where we’re going to store our tasks. It’s like a digital filing cabinet for our data. You can download it from the [PostgreSQL website](https://www.postgresql.org/download/).

psycopg2 Installation:

We need a way for our Django app to talk to PostgreSQL, and `psycopg2` is the bridge.
In your virtual environment, run:

pip install psycopg2-binary

NOTES:
Django: It’s the framework for building web apps.
Django Rest Framework (DRF): It’s the toolkit for creating web APIs.
psycopg2: It’s the link between your app and a PostgreSQL database.
Project Setup
Create a Django Project:
Think of a Django project as a big container for all your code. It’s like the foundation of your house.
To create a project, open your terminal and run:

django-admin startproject tutorial

cd tutorial

Create a Django App:
Apps are like rooms in your house. Each app has a specific purpose.
Create an app for our tasks:

python manage.py startapp movie

Django Configuration
INSTALLED_APPS:
- Apps are like tools in your toolbox. We need to tell Django which tools (apps) we want to use. Open `myproject/settings.py` and add `’rest_framework’` and `’myapp’` to the `INSTALLED_APPS` list.

Let us add it inside the INSTALLED_APPS list:

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
Database Configuration:
Now, we're going to tell our Django project to use the PostgreSQL database we've set up. In the project's settings.py file, you'll find a section called DATABASES. It looks like this:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
We need to replace this SQLite database configuration with the PostgreSQL database we created. So, change the DATABASES section to look like this:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase', #change it databasename
        'USER': 'mydatabaseuser', #change it database user name
        'PASSWORD': 'mypassword', # change user database password
        'HOST': 'localhost',  
        'PORT': '5432',           
    }
}

Replace 'mydatabase', 'mydatabaseuser', and 'mypassword' with your own choices.

Define Models
Task Model

Think of a model as a blueprint for your data. We’ll create a `Movie` model in `myapp/models.py`. It will have fields like `name`, `director`, and `completed`.

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.TextField()
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
Migrations and Database Setup:
This is where we tell Django to create our database tables based on our app’s models.
- Run these commands:

python manage.py makemigrations
python manage.py migrate

Serializers
What Are Serializers?
- Serializers help us convert our complex data (like a `Movie` object) into a format that can be easily sent over the internet. It’s like wrapping a gift to send it to someone.

TaskSerializer:
We’ll create a `MovieSerializer` in `movie/serializers.py`. This tells Django how to turn our `Movie` model into JSON.

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
Views
Views Overview:

Views are like the control center of our app. They decide what happens when you visit a specific URL.
We’ll create views for listing movies, creating movies, updating movies, and deleting movies.

Movie Create, Update, and Delete Views:
These views will handle creating, updating, and deleting tasks.

from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response

class MovieListCreateView(generics.ListCreateAPIView):
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
        
Movie List and Detail Views:
Task List and Detail Views:
These views will handle listing all tasks and showing details of a single task.
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
full views.py file

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
URL Patterns:
first create a urls.py file in your app

To make our views accessible through URLs, we’ll define URL patterns in `movie/urls.py`.

from django.urls import path
from .views import MovieListCreateView, MovieDetailView,AllMoviesListView,MovieDeleteView,MovieUpdateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/all/', AllMoviesListView.as_view(), name='all-movies-list'),  
    path('movies/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'), 
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'), 
]
Project/urls.py
update in your project urls.py file

tutorial/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie.urls')),  # Include your app's URLs
]
Run the Development Server
- Start the development server:

python manage.py runserver

API Endpoints
Endpoint Documentation:
Now, we get to the fun part!

We’ll create API endpoints that allow us to interact with our tasks.
- Here are the key endpoints:
— `GET /api/tasks/` — List all tasks
— `POST /api/tasks/` — Create a new task
— `GET /api/tasks/{task_id}/` — Retrieve a specific task
— `PUT /api/tasks/{task_id}/` — Update a specific task
— `DELETE /api/tasks/{task_id}/` — Delete a specific taskAuthentication and Permissions (if applicable):

We’ll decide who can do what with our API. This is like setting up security gates. For this project, we’ll keep it simple.

Testing
Manual Testing:
We’ll use tools like Postman to test our API. It’s like checking if all the buttons on your remote control work.

Conclusion:
Summary:
We’ve covered a lot of ground in this project. You’ve learned how to set up an environment, create a Django app, define models, create serializers, and build API endpoints. That’s pretty cool!

Future Enhancements:
- There’s so much more you can do with this project. You could add user authentication, handle errors better, or even create a front-end interface. The possibilities are endless!