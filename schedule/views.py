from django.shortcuts import render,redirect
from .models import Match

flags = { 
        "Arabia Saudita": "\U0001f1f8\U0001f1e6",
        "Alemania": "\U0001f1e9\U0001f1ea",
        "Argentina": "\U0001f1e6\U0001f1f7" ,
        "Australia":"\U0001f1e6\U0001f1fa",
        "Belgica": 	"\U0001f1e7\U0001f1ea",
        "Brasil": "\U0001f1e7\U0001f1f7", 
        "Camerun": "\U0001f1e8\U0001f1f2",
        "Canada": "\U0001f1e8\U0001f1e6",
        "Costa Rica" : "\U0001f1e8\U0001f1f7",
        "Corea": "\U0001f1f0\U0001f1f7",  
        "Catar": "\U0001f1f6\U0001f1e6", 
        "Croacia": "\U0001f1ed\U0001f1f7", 
        "Dinamarca": "\U0001f1e9\U0001f1f0",
        "Espana" :"\U0001f1ea\U0001f1f8", 
        "Ecuador": "\U0001f1ea\U0001f1e8",
        "Francia":"\U0001f1eb\U0001f1f7",
        "Ghana": "\U0001f1ec\U0001f1ed",
        "Gales": "	\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f",
        "Holanda":"\U0001f1f3\U0001f1f1",
        "Inglaterra": "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
        "Iran": "\U0001f1ee\U0001f1f7",
        "Japon": "\U0001f1ef\U0001f1f5",
        "Marruecos": "\U0001f1f2\U0001f1e6", 
        "Mexico": "\U0001f1f2\U0001f1fd",
        "Portugal": "\U0001f1f5\U0001f1f9",
        "Polonia": "\U0001f1f5\U0001f1f1",
        "Serbia": "\U0001f1f7\U0001f1f8",
        "Suiza": "\U0001f1e8\U0001f1ed" , 
        "Senegal" : "\U0001f1f8\U0001f1f3",
        "Tunez": "\U0001f1f9\U0001f1f3",  
        "USA": "\U0001f1fa\U0001f1f8",
        "Uruguay": "\U0001f1fa\U0001f1fe",
        



        }

# Create your views here.
def schedule_create_view(request):
    
    match_schedule = [{"id":"1",  "local" : "Catar"      , "visitor" : "Ecuador"},
                      {"id":"2",  "local" : "Senegal"    , "visitor" : "Holanda"},
                      {"id":"3",  "local" : "Inglaterra" , "visitor" : "Iran"},
                      {"id":"4",  "local" : "USA"        , "visitor" : "Gales"},
                      {"id":"5",  "local" : "Francia"    , "visitor" : "Australia"},
                      {"id":"6",  "local" : "Dinamarca"  , "visitor" : "Tunez"},
                      {"id":"7",  "local" : "Mexico"     , "visitor" : "Polonia"},
                      {"id":"8",  "local" : "Argentina"  , "visitor" : "Arabia Saudita"},
                      {"id":"9 ",  "local" : "Belgica"    , "visitor" : "Canada"},
                      {"id":"10",  "local" : "Espana"     , "visitor" : "Costa Rica"},
                      {"id":"11",  "local" : "Alemania"    , "visitor": "Japon"},
                      {"id":"12",  "local" : "Marruecos"  , "visitor" : "Croacia"},
                      {"id":"13",  "local" : "Suiza"      , "visitor" : "Camerun"},
                      {"id":"14",  "local" : "Uruguay"    , "visitor" : "Corea"},
                      {"id":"15",  "local" : "Portugal"   , "visitor" : "Ghana"},
                      {"id":"16",  "local" : "Brasil"     , "visitor" : "Serbia"},
                      {"id":"17",  "local" : "Gales"      , "visitor": "Iran"},
                      {"id":"18",  "local" : "Catar"      , "visitor" : "Senegal"},
                      {"id":"19",  "local" : "Holanda"    , "visitor" : "Ecuador"},
                      {"id":"20",  "local" : "Inglaterra" , "visitor" : "USA"},
                      {"id":"21",  "local" : "Tunez"      , "visitor" : "Australia"},
                      {"id":"22",  "local" : "Polonia"    , "visitor" : "Arabia Saudita"},
                      {"id":"23",  "local" : "Francia"    , "visitor" : "Dinamarca"  },
                      {"id":"24",  "local" : "Argentina"     , "visitor" : "Mexico"},
                      {"id":"25",  "local" : "Japon"      , "visitor": "Costa Rica"},
                      {"id":"26",  "local" : "Belgica"      , "visitor" : "Marruecos"},
                      {"id":"27",  "local" : "Croacia"    , "visitor" : "Canada"},
                      {"id":"28",  "local" : "Espana"      , "visitor" : "Alemania"},
                      {"id":"29",  "local" : "Camerun"    , "visitor" : "Serbia"},
                      {"id":"30",  "local" : "Corea"    , "visitor" : "Ghana"  },
                      {"id":"31",  "local" : "Brasil"     , "visitor" : "Suiza"},
                      {"id":"32",  "local" : "Portugal"      , "visitor": "Uruguay"},
                      {"id":"33",  "local" : "Gales"      , "visitor" : "Inglaterra"},
                      {"id":"34",  "local" : "Iran"    , "visitor" : "USA"},
                      {"id":"35",  "local" : "Ecuador" , "visitor" : "Senegal"},
                      {"id":"36",  "local" : "Holanda" , "visitor" : "Catar"  },
                      {"id":"37",  "local" : "Australia"      , "visitor" : "Dinamarca"},
                      {"id":"38",  "local" : "Tunez"    , "visitor" : "Francia"},
                      {"id":"39",  "local" : "Polonia"    , "visitor" : "Argentina"  },
                      {"id":"40",  "local" : "Arabia Saudita"      , "visitor" : "Mexico"},
                      {"id":"41",  "local" : "Croacia"    , "visitor" : "Belgica"},
                      {"id":"42",  "local" : "Canada"    , "visitor" : "Marruecos"  },
                      {"id":"43",  "local" : "Japon"      , "visitor" : "Espana"},
                      {"id":"44",  "local" : "Costa Rica"    , "visitor" : "Alemania"},
                      {"id":"45",  "local" : "Ghana"    , "visitor" : "Uruguay"  },
                      {"id":"46",  "local" : "Corea"      , "visitor" : "Portugal"},
                      {"id":"47",  "local" : "Serbia"    , "visitor" : "Suiza"},
                      {"id":"48",  "local" : "Camerun"    , "visitor" : "Brasil"  },
    ]

    

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
    match_schedule= []
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
            match_schedule.append(match)
        except:
            pass

        

    context = {
        "list" : match_schedule
    }

    

  
    return render(request, 'schedule/view.html', context)

    