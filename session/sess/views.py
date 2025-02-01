from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import *

def index(request: HttpRequest):
    request.session['name'] = 'Doston'
    context = {
        'news': News.objects.all()
    }
    print(context)
    return render(request, 'index.html', context)

def get_name(request: HttpRequest):
    name = request.session.get('name')
    return HttpResponse(f"{name}")

def delete_name(request: HttpRequest):
    request.session.flush()
    return HttpResponse('Ochirildi')