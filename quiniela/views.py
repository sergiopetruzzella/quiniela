from django.http import HttpResponse
from django.template.loader import render_to_string 
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
import sys
from schedule.models import RealScore

def home_view (request):
    return  render(request, 'home-view.html', {})

def desk_view (request):
    return  render(request, 'desk.html', {})

def admin_manage_view (request):
    
    if request.method == "POST": 
        RealScore.objects.create(
            local_score = request.POST.get("local_score"),
            visitor_score = request.POST.get("visitor_score"),

            id = request.POST.get("match_number"))
    
    all_scores = RealScore.objects.all()
    context =  {"all_scores" : all_scores}




    return  render(request, 'admin/manage.html', context)

