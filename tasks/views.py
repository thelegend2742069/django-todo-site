from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TasksForm

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TasksForm(instance=task)
    context = {'form':form}

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()


    return render(request, 'tasks/update_task.html', context)