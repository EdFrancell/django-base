from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render_to_response, render,redirect


def homepage(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}
	return render_to_response('index.html', context)

