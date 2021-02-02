from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoItem


def index(request):
    todo_items = TodoItem.objects.all()
    print(todo_items)
    for todo_item in todo_items:
        print(todo_item.notes)
    
    context = {
        'todo_items': todo_items
    }
    return render(request, 'todoapp/index.html', context)

