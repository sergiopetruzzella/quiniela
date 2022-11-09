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
    ########################### ACA SE GENERA LA PUNTUACION DE TODOS LOS USUARIOS DE LA PLATAFORMA
    scores = RealScore.objects.all() # Resultados Reales
    users = User.objects.all() # Cargo los Usuarios
    for x in users:
        user_schedule = Match.objects.filter(user_id=x.id) #Extraigo las predicciones de un usuario
        points = 0 
        for i in scores:  #recorro cada juego 
            try:
                us = user_schedule.get(match_number=i.id) #user Score
                user_result = (-us.local_score + us.visitor_score)/abs(us.local_score - us.visitor_score)
                real_result = (-i.local_score + i.visitor_score)/abs(i.local_score - i.visitor_score)
                user_goal_diference = -us.local_score + us.visitor_score
                real_goal_diference = -i.local_score + i.visitor_score
                goals_diference_error  = abs(user_goal_diference - real_goal_diference)
                
                if user_result == real_result : 
                    points += 4 # 4 puntos por acertar vencedor
                elif goals_diference_error == 1:
                    points+= 1  # 1 1 punto de comodin
                
                if us.local_score == i.local_score:
                    points+= 1 #punto por acertar goles del local
                
                if us.visitor_score == i.visitor_score:
                    points+= 1 #punto por acertar goles del visitante
                
                if user_goal_diference == real_goal_diference:
                    points+= 1 #punto por acertar diferencia de goles
            except:
                pass
        try:    
            UserScore.objects.get(user=x).delete()
        except:
            pass
        UserScore.objects.create(user=x,points=points)
    x = UserScore.objects.order_by("-points")    
    return  render(request, 'admin/table.html', {"list": x})
