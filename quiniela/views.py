from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import sys
from schedule.models import RealScore, Match, UserScore


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


def generate_points (request):
    scores = RealScore.objects.all()
    users = User.objects.all()
    for x in users:
        user_schedule = Match.objects.filter(user_id=x.id)
        points = 0 
        for i in scores:
            try:
                us = user_schedule.get(match_number=i.id) #user Score
                user_result = (-us.local_score + us.visitor_score)/abs(us.local_score - us.visitor_score)
                real_result = (-i.local_score + i.visitor_score)/abs(i.local_score - i.visitor_score)
                if user_result == real_result : points += 1 
            except:
                pass
        try:    
            UserScore.objects.get(user=x).delete()
        except:
            pass
        UserScore.objects.create(user=x,points=points)
    x = UserScore.objects.order_by("-points")    
    return  render(request, 'admin/table.html', {"list": x})
