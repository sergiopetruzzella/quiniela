from django.http import HttpResponse
from django.template.loader import render_to_string 
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout

def home_view (request):
    return  render(request, 'home-view.html', {})

def desk_view (request):
    return  render(request, 'desk.html', {})

def admin_manage_view (request):
    return  render(request, 'admin-manage.html', {})
