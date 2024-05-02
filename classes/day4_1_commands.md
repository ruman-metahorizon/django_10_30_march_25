## Run command:

`
django-admin startapp accounts

`

## Insall app accounts to blogs/setting.py

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'boards',
    'accounts',
]
`


## Add following code to blogs/urls.py


`

from accounts import views as accounts_views

urlpatterns = [

    re_path(r'^signup/$', accounts_views.signup, name='signup'),

]
`

## Add following code to accounts/views.py

`
def signup(request):
    return render(request, 'signup.html')

`

## Create a new file templates/signup.html and Add following code:

`
{% extends 'base.html' %}

{% block content %}
  <h2>Sign up</h2>
{% endblock %}
`

## Add following testcases to accounts/tests.py

`

from .views import signup
from django.urls import resolve, reverse

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)
`


## Make changes to base.html

`

{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
    {% block stylesheet %}{% endblock %}  <!-- HERE -->
  </head>
  <body>
    {% block body %}  <!-- HERE -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
        </div>
      </nav>
      <div class="container">
        <ol class="breadcrumb my-4">
          {% block breadcrumb %}
          {% endblock %}
        </ol>
        {% block content %}
        {% endblock %}
      </div>
    {% endblock body %}  <!-- AND HERE -->
  </body>
</html>
`


## Add following code to accounts/views.py

`
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
`


## Add following code to signup.html

`

{% block body %}
  <div class="container">
    <h2>Sign up</h2>
    <form method="post" novalidate>
      {% csrf_token %}
      {% include 'includes/form.html' %}
      <button type="submit" class="btn btn-primary">Create an account</button>
    </form>
  </div>
{% endblock %}
`

## Add following code to accounts/view.py


`

from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
`