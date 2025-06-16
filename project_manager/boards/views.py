from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'boards/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.tasks.all()
    form = TaskForm()
    return render(request, 'boards/project_detail.html', {
        'project': project,
        'tasks': tasks,
        'form': form
    })

@login_required
def add_task(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
    return redirect('project_detail', pk=pk)
