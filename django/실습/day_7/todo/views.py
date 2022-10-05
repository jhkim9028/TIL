from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.order_by('priority')
    context = {
        'todos':todos,
    }
    return render(request,'todo/index.html',context)

def create(request):
    todo = request.GET.get('todo_')
    priority = request.GET.get('rank')
    deadline = request.GET.get('deadline')
    
    Todo.objects.create(content=todo, priority=priority, daedline=deadline)
    return redirect('todo:index')

def delete(request,pk):
    todo_d = Todo.objects.get(pk=pk)
    todo_d.delete()
    
    return redirect('todo:index')

def update(request,pk):
    todo = Todo.objects.get(pk=pk)
    
    completed_ = True
    
    todo.completed = completed_
    
    todo.save()
    
    return redirect('todo:index')