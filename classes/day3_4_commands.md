### Add following code to base.html

`
<link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
<link rel="stylesheet" href="{% static 'css/app.css' %}">
`

## Create a new file static/css/app.css

`
.navbar-brand {
    font-family: 'Peralta', cursive;
  }
`

## Add following code to blogs/urls.py
`
re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
`

## Add following code to boards/views.py
`
from django.shortcuts import render, get_object_or_404

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
`

## Create a  new html template in templates directory called new_topic.html
`
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}

{% endblock %}
`

## Add test cases for NewTopic:
`
from .views import home, board_topics, new_topic

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))
`

## Add following code to new_topic.html

`
{% block content %}
  <form method="post">
    {% csrf_token %}
    <div class="form-group">
      <label for="id_subject">Subject</label>
      <input type="text" class="form-control" id="id_subject" name="subject">
    </div>
    <div class="form-group">
      <label for="id_message">Message</label>
      <textarea class="form-control" id="id_message" name="message" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
`
