### Add following code for testcase:
`
boards/tests.py

from django.urls import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
`

### Run command to test:
`
python manage.py test
`

## HTTP Codes

[HTTP Status Code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### More testcases:

`
from django.urls import reverse, resolve
from .views import home

def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
`

## Run command for details:
`
python manage.py test --verbosity=2
`

## Add following code to settings.py
`
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
`

## Add following code to templates/home.html
`

{% load static %}

and add to head:

<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
`