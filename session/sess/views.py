from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest):
    request.session['name'] = 'Doston'
    return HttpResponse(f"{request.user.username}")

def get_name(request: HttpRequest):
    name = request.session.get('name')
    return HttpResponse(f"{name}")

def delete_name(request: HttpRequest):
    request.session.flush()
    return HttpResponse('Ochirildi')