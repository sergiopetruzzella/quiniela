from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
import sys
from schedule.models import RealScore, Match, UserScore

flags = { 
        "Arabia Saudita": "\U0001f1f8\U0001f1e6",
        "Alemania": "\U0001f1e9\U0001f1ea",
        "Argentina": "\U0001f1e6\U0001f1f7" ,
        "Australia":"\U0001f1e6\U0001f1fa",
        "Bélgica": 	"\U0001f1e7\U0001f1ea",
        "Brasil": "\U0001f1e7\U0001f1f7", 
        "Camerún": "\U0001f1e8\U0001f1f2",
        "Canadá": "\U0001f1e8\U0001f1e6",
        "Costa Rica" : "\U0001f1e8\U0001f1f7",
        "Corea": "\U0001f1f0\U0001f1f7",  
        "Catar": "\U0001f1f6\U0001f1e6", 
        "Croacia": "\U0001f1ed\U0001f1f7", 
        "Dinamarca": "\U0001f1e9\U0001f1f0",
        "España" :"\U0001f1ea\U0001f1f8", 
        "Ecuador": "\U0001f1ea\U0001f1e8",
        "Francia":"\U0001f1eb\U0001f1f7",
        "Ghana": "\U0001f1ec\U0001f1ed",
        "Gales": "	\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f",
        "Holanda":"\U0001f1f3\U0001f1f1",
        "Inglaterra": "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
        "Irán": "\U0001f1ee\U0001f1f7",
        "Japón": "\U0001f1ef\U0001f1f5",
        "Marruecos": "\U0001f1f2\U0001f1e6", 
        "México": "\U0001f1f2\U0001f1fd",
        "Portugal": "\U0001f1f5\U0001f1f9",
        "Polonia": "\U0001f1f5\U0001f1f1",
        "Serbia": "\U0001f1f7\U0001f1f8",
        "Suiza": "\U0001f1e8\U0001f1ed" , 
        "Senegal" : "\U0001f1f8\U0001f1f3",
        "Túnez": "\U0001f1f9\U0001f1f3",  
        "USA": "\U0001f1fa\U0001f1f8",
        "Uruguay": "\U0001f1fa\U0001f1fe",
        "":""
        
}

def home_view (request):
    return  render(request, 'home-view.html', {})

def desk_view (request):
    user = request.user 
    user_groups = user.groups.all()
    rsc=  RealScore.objects.count() #RealScoresCount
    users_scores = UserScore.objects.order_by("-points")
    n_mts = Match.objects.filter(user_id = request.user.id)[rsc:10+rsc]
    next_matches = []
    for i in n_mts:
        try:
            match = {
                "local" : i.local ,  
                "visitor" : i.visitor  , 
                "local_score": i.local_score,
                "visitor_score": i.visitor_score,
                "lf" : flags[i.local], 
                "vf" : flags[i.visitor],
            }
            next_matches.append(match)
        except:
            pass
    
    
    
    context = {"list": users_scores,
                "matches": next_matches,
                "user_groups": user_groups,
                }
    

    return  render(request, 'desk.html', context)

def admin_manage_view (request):   
    if not request.user.is_superuser: 
        return render(request, 'forbidden.html', {})


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
                try:
                    user_result = (-us.local_score + us.visitor_score)/abs(us.local_score - us.visitor_score)
                except:
                    user_result = 0
                try: 
                    real_result = (-i.local_score + i.visitor_score)/abs(i.local_score - i.visitor_score)
                except:
                    real_result = 0 
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
    data =[]
    for i in x :
        user_match_count = Match.objects.filter(user_id= i.user.id).count()
        data.append({"points": i.points, "user": i.user.username, "count" : user_match_count})
       
    return  render(request, 'admin/ado-table.html', {"list": data})


def info_view (request): 

    return render(request, 'info.html', {})

def user_puntuation (request,user):
    error = None
    try:
        try:
            username = User.objects.get(username=user)
        except:
            slug = user +" "
            username = User.objects.get(username=slug)
        matches  = Match.objects.filter(user_id = username.id)  
        real_scores      = RealScore.objects.all()
    except User.DoesNotExist:
        username  = None
        error = "Usuario no encontrado"
    data = []
    if username :
        for i in matches:
            try:
               r_s = real_scores.get(id=i.match_number)
               try:
                   real_result = (-r_s.local_score + r_s.visitor_score)/abs(r_s.local_score - r_s.visitor_score)
               except:
                   real_result = 0 
               try: 
                   user_result = (-i.local_score + i.visitor_score)/abs(i.local_score - i.visitor_score)
               except:
                   user_result=0 
               user_goal_diference = -i.local_score + i.visitor_score
               real_goal_diference = -r_s.local_score + r_s.visitor_score
               goals_diference_error  = abs(user_goal_diference - real_goal_diference)
               points  = 0 
               print(points)
               if user_result == real_result : 
                   points += 4 # 4 puntos por acertar vencedor
               elif goals_diference_error == 1:
                   points+= 1  # 1 1 punto de comodin

               if i.local_score == r_s.local_score:
                   points+= 1 #punto por acertar goles del local

               if i.visitor_score == r_s.visitor_score:
                   points+= 1 #punto por acertar goles del visitante

               if user_goal_diference == real_goal_diference:
                   points+= 1 #punto por acertar diferencia de goles
               data.append({
                   "local" : i.local ,
                   "local_flag": flags[i.local],
                   "local_score": i.local_score,
                   "visitor": i.visitor,
                   "visitor_score": i.visitor_score,
                   "visitor_flag": flags[i.visitor],
                   "real_local_score"  : r_s.local_score,
                   "real_visitor_score": r_s.visitor_score, 
                   "points": points

               })
            except: 
                data.append({
                   "local" : i.local ,
                   "local_score": i.local_score,
                   "visitor": i.visitor,
                   "visitor_score": i.visitor_score,
                    "local_flag": flags[i.local],
                    "visitor_flag": flags[i.visitor],


               })

            teams_info = []
            cont = 0
            for i  in matches:
                if i.local not in map(lambda x: x["name"] , teams_info ):
                    cont+=1
                    teams_info.append({"name":i.local , "pts": 0 , "mw": 0, "md": 0, "ml": 0,  "gs": 0, "gr": 0, "gd": 0})
            
                if i.visitor not in map(lambda x: x["name"] , teams_info ):
                    cont+=1
                    teams_info.append({"name":i.visitor, "pts": 0 , "mw": 0, "md": 0, "ml": 0,  "gs": 0, "gr": 0, "gd": 0})
        
                local_index = next((index for (index, d) in enumerate(teams_info) if d["name"] == i.local), None)
                visitor_index = next((index for (index, d) in enumerate(teams_info) if d["name"] == i.visitor), None)
                gd = -i.local_score + i.visitor_score
                if gd<0 :
                    teams_info[local_index]["pts"]+=3
                    teams_info[local_index]["mw"]+=1
                    teams_info[visitor_index]["ml"]+=1
                elif gd>0 :
                    teams_info[visitor_index]["pts"]+=3
                    teams_info[local_index]["ml"]+=1
                    teams_info[visitor_index]["mw"]+=1
                else:
                    teams_info[visitor_index]["pts"]+=1
                    teams_info[local_index]["pts"]+=1
                    teams_info[local_index]["md"]+=1
                    teams_info[visitor_index]["md"]+=1
                teams_info[local_index]["gs"]+= i.local_score
                teams_info[local_index]["gr"]+= i.visitor_score
                teams_info[visitor_index]["gs"]+= i.visitor_score
                teams_info[visitor_index]["gr"]+= i.local_score
                teams_info[local_index]["gd"]-= gd
                teams_info[visitor_index]["gd"]+= gd
                        

        teams_info.sort(key=lambda x: (-x["pts"], -x["gd"], -x["gs"]))

        groups = [ {"name":"A", "teams": ["Catar", "Ecuador" , "Senegal", "Holanda" ] , "data": [] , "qual": ["Holanda", "Senegal"] },
                {"name":"B", "teams": ["Inglaterra", "USA" , "Gales", "Irán"] , "data": [] , "qual": ["Inglaterra", "USA" ] },
                {"name":"C", "teams": ["Argentina","Polonia","Arabia Saudita","México"] , "data": [] , "qual": ["Argentina","Polonia"] },
                {"name":"D", "teams": ["Francia","Dinamarca","Australia","Túnez"] , "data": [] , "qual": ["Francia","Australia"] },
                {"name":"E", "teams": ["España","Alemania","Costa Rica","Japón"] , "data": [] , "qual": ["",""] },
                {"name":"F", "teams": ["Bélgica","Croacia","Canadá","Marruecos"] , "data": [] , "qual": ["",""] },
                {"name":"G", "teams": ["Brasil","Serbia","Suiza","Camerún"] , "data": [] , "qual": ["",""] },
                {"name":"H", "teams": ["Portugal","Uruguay","Corea","Ghana"] , "data": [] , "qual": ["",""] },
            ]
        for team in teams_info:
            for group in groups: 
                if team["name"] in group["teams"] and len (group["data"]) < 2 :
                    pts = 0
                    team_id =  len (group["data"]) 
                    if team["name"] == group["qual"][team_id]:
                        pts += 4
                    if team["name"] in group["qual"]:
                        pts += 4                   
                    
                    pos = { "pred"  : team["name"],
                            "pflag" : flags[team["name"]],
                            "real"  : group["qual"][team_id],
                            "rflag" : flags[group["qual"][team_id]],
                            "pts"   : pts 
                            }
            
                    
                    group["data"].append(pos)


        context = {"user":username,
                "data": data,
                "groups" :groups , 
        
        }
        
    return render(request,  'accounts/puntuation.html', context)


def generate_points_by_groups (request):

    users = User.objects.all() # Cargo los Usuarios
    for x in users:
        u_sche = Match.objects.filter(user_id = x.id)
        if u_sche.count() <48 :
            continue
        teams_info = []
        cont = 0
        for i  in u_sche:
            if i.local not in map(lambda x: x["name"] , teams_info ):
                cont+=1
                teams_info.append({"name":i.local , "pts": 0 , "mw": 0, "md": 0, "ml": 0,  "gs": 0, "gr": 0, "gd": 0})
        
            if i.visitor not in map(lambda x: x["name"] , teams_info ):
                cont+=1
                teams_info.append({"name":i.visitor, "pts": 0 , "mw": 0, "md": 0, "ml": 0,  "gs": 0, "gr": 0, "gd": 0})
    
            local_index = next((index for (index, d) in enumerate(teams_info) if d["name"] == i.local), None)
            visitor_index = next((index for (index, d) in enumerate(teams_info) if d["name"] == i.visitor), None)
            gd = -i.local_score + i.visitor_score
            if gd<0 :
                teams_info[local_index]["pts"]+=3
                teams_info[local_index]["mw"]+=1
                teams_info[visitor_index]["ml"]+=1
            elif gd>0 :
                teams_info[visitor_index]["pts"]+=3
                teams_info[local_index]["ml"]+=1
                teams_info[visitor_index]["mw"]+=1
            else:
                teams_info[visitor_index]["pts"]+=1
                teams_info[local_index]["pts"]+=1
                teams_info[local_index]["md"]+=1
                teams_info[visitor_index]["md"]+=1
            teams_info[local_index]["gs"]+= i.local_score
            teams_info[local_index]["gr"]+= i.visitor_score
            teams_info[visitor_index]["gs"]+= i.visitor_score
            teams_info[visitor_index]["gr"]+= i.local_score
            teams_info[local_index]["gd"]-= gd
            teams_info[visitor_index]["gd"]+= gd
                    

        teams_info.sort(key=lambda x: (-x["pts"], -x["gd"], -x["gs"]))

        groups = [ {"name":"A", "teams": ["Catar", "Ecuador" , "Senegal", "Holanda" ] , "data": [] , "qual": ["Holanda", "Senegal"] },
               {"name":"B", "teams": ["Inglaterra", "USA" , "Gales", "Irán"] , "data": [] , "qual": ["Inglaterra", "USA" ] },
               {"name":"C", "teams": ["Argentina","Polonia","Arabia Saudita","México"] , "data": [] , "qual": ["Argentina","Polonia"] },
               {"name":"D", "teams": ["Francia","Dinamarca","Australia","Túnez"] , "data": [] , "qual": ["Francia","Australia"] },
               {"name":"E", "teams": ["España","Alemania","Costa Rica","Japón"] , "data": [] , "qual": ["",""] },
               {"name":"F", "teams": ["Bélgica","Croacia","Canadá","Marruecos"] , "data": [] , "qual": ["",""] },
               {"name":"G", "teams": ["Brasil","Serbia","Suiza","Camerún"] , "data": [] , "qual": ["",""] },
               {"name":"H", "teams": ["Portugal","Uruguay","Corea","Ghana"] , "data": [] , "qual": ["",""] },
        ]
        for team in teams_info:
            for group in groups:  
                if team["name"] in group["teams"]:
                    group["data"].append(team)

        pts = 0 
        for group in groups:
            for team_id in range(2):
                if group["data"][team_id]["name"] == group["qual"][team_id]:
                    pts += 4
                if group["data"][team_id]["name"] in group["qual"]:
                    pts += 4

        try:    
            score = UserScore.objects.get(user=x)
            score.points += pts
            print(score.points)
            score.save() 

        except: 
            pass

    x = UserScore.objects.order_by("-points") 
    data =[]
    for i in x :
        user_match_count = Match.objects.filter(user_id= i.user.id).count()
        data.append({"points": i.points, "user": i.user.username, "count" : user_match_count})
        

    

    return  render(request, 'admin/ado-table.html', {"list": data} )

    
    