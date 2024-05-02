### Information on HTTP requests:
[request_methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)


## Add following code to boards/views.py
`
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})

`

## Add following code to templates/topics.html

`
{% block content %}
<div class="mb-4">
    <a href="{% url 'new_topic' board.pk %}" class="btn btn-primary">New topic</a>
  </div>
  
<table class="table">
  <thead class="thead-inverse">
    <tr>
      <th>Topic</th>
      <th>Starter</th>
      <th>Replies</th>
      <th>Views</th>
      <th>Last Update</th>
    </tr>
  </thead>
  <tbody>
    {% for topic in board.topics.all %}
    <tr>
      <td>{{ topic.subject }}</td>
      <td>{{ topic.starter.username }}</td>
      <td>0</td>
      <td>0</td>
      <td>{{ topic.last_updated }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock %}
`