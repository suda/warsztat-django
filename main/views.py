# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .forms import PhotoForm
from .models import Photo

def hello(request):
	return render(request, 'index.html', {
        'title': u'ostatnie zdjęcia',
        'photos': Photo.objects.filter(published=True).order_by('-date')        
    })

def hello_name(request, name):
	return HttpResponse('Hello %s!' % name)

@login_required
def upload(request):
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.user = request.user			
			form.instance.published = True
			form.save()
			messages.success(request, u'Zdjęcie załadowane')
			return redirect(reverse('hello'))
		else:
			messages.error(request, u'Proszę poprawić formularz')
			
	else:
		form = PhotoForm()

	return render(request, 'upload.html', {
        'title': u'przesyłanie zdjęć',
        'form': form
    })