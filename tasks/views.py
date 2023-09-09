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