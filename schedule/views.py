from django.shortcuts import render,redirect
from .models import Schedule, Match



# Create your views here.
def schedule_create_view(request):
    
    match_schedule = [{"id":"1",  "local" : "Catar"      , "visitor" : "Ecuador"},
                      {"id":"2",  "local" : "Senegal"    , "visitor" : "Holanda"},
                      {"id":"3",  "local" : "Inglaterra" , "visitor" : "Iran"},
                      {"id":"4",  "local" : "USA"        , "visitor" : "Gales"},
                      {"id":"5",  "local" : "Francia"    , "visitor" : " Austria"},
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
        

    context = {"list" :  match_schedule }
    return  render(request, 'schedule/create.html', context)

    