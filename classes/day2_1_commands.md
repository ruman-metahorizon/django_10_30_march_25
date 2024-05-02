# Added the following code:
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

## Commands Used:

`
python manage.py shell

from boards.models import Board

Board.objects.all()

boards_list = Board.objects.all()
for board in boards_list:
    print(board.description)

django_board = Board.objects.get(id=1)

django_board.name
django_board.description

django = Board.objects.get(name='Django')
django.name


board = Board(name='Django updated', description='This is a board about Django.', id=1)
board.save()


`

### ADD following code to boards/views.py
`
from .models import Board
def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
`

### Add templates to setttings.py
`
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
`

### Remove the code in home.html:

`
    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}
`
### And add the following table code:
`
<table border="1">
      <thead>
        <tr>
          <th>Board</th>
          <th>Posts</th>
          <th>Topics</th>
          <th>Last Post</th>
        </tr>
      </thead>
      <tbody>
        {% for board in boards %}
          <tr>
            <td>
              {{ board.name }}<br>
              <small style="color: #888">{{ board.description }}</small>
            </td>
            <td>0</td>
            <td>0</td>
            <td></td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
`
