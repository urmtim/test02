from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main\index.html', {'title': 'Главная страница',
                                               'tasks': tasks, })


def info(request):
    return render(request, 'main\info.html', {'title': 'О нас'})


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка данных"
    form = TaskForm()
    return render(request, 'main\create.html', {'title': 'Создать запись',
                                                'form': form,
                                                'error': error,
                                                })