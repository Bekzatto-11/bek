from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'boards/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'boards/project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'boards/project_form.html', {'form': form})