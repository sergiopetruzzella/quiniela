from django.shortcuts import render,redirect
from .models import Match

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
        }




match_schedule = [  {"id":"1",  "local" : "Catar"      , "visitor" : "Ecuador"},
                    {"id":"2",  "local" : "Senegal"    , "visitor" : "Holanda"},
                    {"id":"3",  "local" : "Inglaterra" , "visitor" : "Irán"},
                    {"id":"4",  "local" : "USA"        , "visitor" : "Gales"},
                    {"id":"5",  "local" : "Francia"    , "visitor" : "Australia"},
                    {"id":"6",  "local" : "Dinamarca"  , "visitor" : "Túnez"},
                    {"id":"7",  "local" : "México"     , "visitor" : "Polonia"},
                    {"id":"8",  "local" : "Argentina"  , "visitor" : "Arabia Saudita"},
                    {"id":"9",  "local" : "Bélgica"    , "visitor" : "Canadá"},
                    {"id":"10",  "local" : "España"     , "visitor" : "Costa Rica"},
                    {"id":"11",  "local" : "Alemania"    , "visitor": "Japón"},
                    {"id":"12",  "local" : "Marruecos"  , "visitor" : "Croacia"},
                    {"id":"13",  "local" : "Suiza"      , "visitor" : "Camerún"},
                    {"id":"14",  "local" : "Uruguay"    , "visitor" : "Corea"},
                    {"id":"15",  "local" : "Portugal"   , "visitor" : "Ghana"},
                    {"id":"16",  "local" : "Brasil"     , "visitor" : "Serbia"},
                    {"id":"17",  "local" : "Gales"      , "visitor": "Irán"},
                    {"id":"18",  "local" : "Catar"      , "visitor" : "Senegal"},
                    {"id":"19",  "local" : "Holanda"    , "visitor" : "Ecuador"},
                    {"id":"20",  "local" : "Inglaterra" , "visitor" : "USA"},
                    {"id":"21",  "local" : "Túnez"      , "visitor" : "Australia"},
                    {"id":"22",  "local" : "Polonia"    , "visitor" : "Arabia Saudita"},
                    {"id":"23",  "local" : "Francia"    , "visitor" : "Dinamarca"  },
                    {"id":"24",  "local" : "Argentina"     , "visitor" : "México"},
                    {"id":"25",  "local" : "Japón"      , "visitor": "Costa Rica"},
                    {"id":"26",  "local" : "Bélgica"      , "visitor" : "Marruecos"},
                    {"id":"27",  "local" : "Croacia"    , "visitor" : "Canadá"},
                    {"id":"28",  "local" : "España"      , "visitor" : "Alemania"},
                    {"id":"29",  "local" : "Camerún"    , "visitor" : "Serbia"},
                    {"id":"30",  "local" : "Corea"    , "visitor" : "Ghana"  },
                    {"id":"31",  "local" : "Brasil"     , "visitor" : "Suiza"},
                    {"id":"32",  "local" : "Portugal"      , "visitor": "Uruguay"},
                    {"id":"33",  "local" : "Gales"      , "visitor" : "Inglaterra"},
                    {"id":"34",  "local" : "Irán"    , "visitor" : "USA"},
                    {"id":"35",  "local" : "Ecuador" , "visitor" : "Senegal"},
                    {"id":"36",  "local" : "Holanda" , "visitor" : "Catar"  },
                    {"id":"37",  "local" : "Australia"      , "visitor" : "Dinamarca"},
                    {"id":"38",  "local" : "Túnez"    , "visitor" : "Francia"},
                    {"id":"39",  "local" : "Polonia"    , "visitor" : "Argentina"  },
                    {"id":"40",  "local" : "Arabia Saudita"      , "visitor" : "México"},
                    {"id":"41",  "local" : "Croacia"    , "visitor" : "Bélgica"},
                    {"id":"42",  "local" : "Canadá"    , "visitor" : "Marruecos"  },
                    {"id":"43",  "local" : "Japón"      , "visitor" : "España"},
                    {"id":"44",  "local" : "Costa Rica"    , "visitor" : "Alemania"},
                    {"id":"45",  "local" : "Ghana"    , "visitor" : "Uruguay"  },
                    {"id":"46",  "local" : "Corea"      , "visitor" : "Portugal"},
                    {"id":"47",  "local" : "Serbia"    , "visitor" : "Suiza"},
                    {"id":"48",  "local" : "Camerún"    , "visitor" : "Brasil"  },
    ]

# Create your views here.
def schedule_create_view(request):
   
    for i in match_schedule:
        try:
            i["lf"] = flags[i['local']] 
        except: 
            pass
        try: 
            i["vf"] = flags[i['visitor']]
        except: 
            pass
        

    if request.method == "POST":
        print (request.POST)

        Match.objects.filter(user_id=request.user.id).delete()
        print('bien aca')
        for x in match_schedule:
            game = Match.objects.create(
                local=x["local"], 
                local_score=request.POST.get("local"+x["id"]),
                visitor = x["visitor"],
                visitor_score=request.POST.get("visitor"+x["id"]),
                user_id = request.user.id   , 
                match_number = x["id"],
                )

            print(game.local, game.local_score, game.visitor, game.visitor_score)
        print(request.user.id)     
        return redirect('/desk/')
        

    context = {"list" :  match_schedule, "flags" :flags}
    return  render(request, 'schedule/create.html', context)


    
def schedule_view_selections(request):
    u_sch = Match.objects.filter(user_id = request.user.id)
    match_sch= []
    for i in u_sch:
        try:
            match = {
                "local" : i.local ,  
                "visitor" : i.visitor  , 
                "local_score": i.local_score,
                "visitor_score": i.visitor_score,
                "lf" : flags[i.local], 
                "vf" : flags[i.visitor],
            }
            match_sch.append(match)
        except:
            pass   

    context = {
        "matches" : match_sch
    }

    return render(request, 'schedule/view.html', context)


    
def schedule_edit_selections (request):
    u_sch = Match.objects.filter(user_id = request.user.id)
    match_sch= []
    for i in u_sch:
        try:
            match = {
                "local" : i.local ,  
                "visitor" : i.visitor  , 
                "local_score": i.local_score,
                "visitor_score": i.visitor_score,
                "lf" : flags[i.local], 
                "vf" : flags[i.visitor],
                "id" : i.match_number
            }
            match_sch.append(match)
        except:
            pass

    context = {
        "matches" : match_sch
    }

    return render(request, 'schedule/edit.html', context)
    

def schedule_group_board_selections (request):
    u_sche = Match.objects.filter(user_id = request.user.id)
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

    groups = [ {"name":"A", "teams": ["Catar", "Ecuador" , "Senegal", "Holanda" ] , "data": []  },
               {"name":"B", "teams": ["Inglaterra", "USA" , "Gales", "Irán"] , "data": [] },
               {"name":"C", "teams": ["Argentina","Polonia","Arabia Saudita","México"] , "data": [] },
               {"name":"D", "teams": ["Francia","Dinamarca","Australia","Túnez"] , "data": [] },
               {"name":"E", "teams": ["España","Alemania","Costa Rica","Japón"] , "data": [] },
               {"name":"F", "teams": ["Bélgica","Croacia","Canadá","Marruecos"] , "data": [] },
               {"name":"G", "teams": ["Brasil","Serbia","Suiza","Camerún"] , "data": [] },
               {"name":"H", "teams": ["Portugal","Uruguay","Corea","Ghana"] , "data": [] },
        ]
    for i in teams_info:
        for j in groups:  
            if i["name"] in j["teams"]:
                i["flag"]= flags[i["name"]]
                j["data"].append(i)
    
        #teams_info[local_index,visitor_index]["gs"] += 1,2
        

    context = {
               "groups": groups 
                }
    return render(request, 'schedule/board.html', context)