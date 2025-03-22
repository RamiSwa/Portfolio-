from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    all_projects = Project.objects.prefetch_related('technologies', 'images').all()
    featured_projects = all_projects.filter(is_featured=True)
    non_featured_projects = all_projects  # we want to show all projects in grid too

    return render(request, 'projects/project_list.html', {
        'featured_projects': featured_projects,
        'projects': non_featured_projects
    })


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('technologies', 'images'), slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})
