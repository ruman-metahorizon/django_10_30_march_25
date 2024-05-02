## update topic_posts.html

`
<a href="{% url 'reply_topic' topic.board.pk topic.pk %}" class="btn btn-primary" role="button">Reply</a>
`

## run command:

*pip install markdown*


## update boards/models.py

`
from django.utils.html import mark_safe
from markdown import markdown

def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

        `


## update topic_posts.html and reply_topic.html

`   
{{ post.get_message_as_markdown }}
`

## update base.html

`
{% block javascript %}{% endblock %}

`

## update reply_topic.html adn edit_post.html


`

{% block stylesheet %}
  <link rel="stylesheet" href="{% static 'css/simplemde.min.css' %}">
{% endblock %}

{% block javascript %}
  <script src="{% static 'js/simplemde.min.js' %}"></script>
  <script>
    var simplemde = new SimpleMDE();
  </script>
{% endblock %}
`


## update edit_post.html

`
{% load static %}
`

## add code to settings.py

`
'django.contrib.humanize',
`

## Create file boards/templatetags/gravatar.py

`

import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url

`

1133

