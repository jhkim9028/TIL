from queue import PriorityQueue
from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.create(content=whattodo, priority=rank)
    todo = Todo.objects.all()
    context = {
        'todo': todo,
    }
    print(todo)
    return redirect('todo:index')