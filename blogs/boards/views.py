from django.shortcuts import render

from django.http import HttpResponse

from .models import Board

def home(request):
    boards = Board.objects.all()
    # boards_names = []

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # return HttpResponse("List of board topics")
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})

def about(request):
    # do something...
    return render(request, 'about.html')
