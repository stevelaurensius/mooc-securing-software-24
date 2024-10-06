from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import File


@login_required
def deleteView(request):
	file = File.objects.get(pk=request.POST.get('id'))
	if file.owner == request.user:
		file.delete()
		return redirect('/')
	else:
		return HttpResponse('You are unauthorized', status=401)
	

@login_required
def downloadView(request, fileid):
	file = File.objects.get(pk=fileid)
	if file.owner == request.user:
		filename = file.data.name.split('/')[-1]
		response = HttpResponse(file.data, content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=%s' % filename
		return response
	else:
		return HttpResponse('You are unauthorized', status=401)


@login_required
def addView(request):
	data = request.FILES.get('file')
	f = File(owner=request.user, data=data)
	f.save()
	return redirect('/')


@login_required
def homePageView(request):
	files = File.objects.filter(owner=request.user)
	uploads = [{'id': f.id, 'name': f.data.name.split('/')[-1]} for f in files]	
	return render(request, 'pages/index.html', {'uploads': uploads})
