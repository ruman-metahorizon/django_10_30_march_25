### Add the following code to boards/views.py
`

def board_topics(request, pk):
    # return HttpResponse("List of board topics")
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
`

### Add the following code to blogs/urls.py
`
re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
`