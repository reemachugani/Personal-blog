from projects.models import Project 
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def projects_home(request):
	projects = Project.objects.all()
	projects1 = []
	projects2 = []
	if projects.count() > 3:
		projects1 = projects[:3]
		projects2 = projects[3:]
	return render_to_response('projects/projects_home.html', {'projects': projects, 'projects1':projects1, 'projects2':projects2}, context_instance=RequestContext(request))