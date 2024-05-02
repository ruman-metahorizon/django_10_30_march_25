### Regex 

## Add following code to blogs/urls.py

`
    re_path(r'^questions/(?P<pk>\d+)/$', views.question, name='question'),
    re_path(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post'),
    re_path(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post'),
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year'),
`

## Add following code to blogs/views.py
`

def question(request, pk):
    return HttpResponse(f"Question : {pk}")


def post(request, slug):
    return HttpResponse(f"Slug : {slug}")

def blog_post(request, slug, pk):
    return HttpResponse(f"Blog_post : {slug} and PK : {pk}")

def user_profile(request, username):
    return HttpResponse(f"User Name : {username}")

def year_archive(request, year):
    return HttpResponse(f"Year: {year}")
`


## Create base.html in templates folder and add following code:

`
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
`

## At home.html file remove all code above html and add following code

`
{% extends 'base.html' %}

{% block breadcrumb %}
<li class="breadcrumb-item active">Boards</li>
{% endblock %}

{% block content %}
`
Also remove code after </table>


## Change the topics.html to :

`
{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
        <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
        <li class="breadcrumb-item active">{{ board.name }}</li>

{% endblock %}

{% block content %}
    <!-- just leaving it empty for now. we will add core here soon. -->
{% endblock %}
`


## Add nav bar to base.html file

`
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
        </div>
    </nav>
`