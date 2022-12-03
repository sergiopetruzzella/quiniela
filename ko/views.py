from django.shortcuts import render, redirect
from .models import KOMatch


# Create your views here.





def ko_create_view(request):

    octavos = [         {"id":"1",  "local" : "Holanda"    , "visitor" : "USA"      , "lf":  "\U0001f1f3\U0001f1f1" , "vf":"\U0001f1fa\U0001f1f8"},
                        {"id":"2",  "local" : "Argentina"  , "visitor" : "Australia", "lf": "\U0001f1e6\U0001f1f7"  , "vf":"\U0001f1e6\U0001f1fa"},
                        {"id":"3",  "local" : "Inglaterra" , "visitor" : "Senegal" , "lf": "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f" , "vf":"\U0001f1f8\U0001f1f3"},
                        {"id":"4",  "local" : "Francia"    , "visitor" : "Polonia", "lf": "\U0001f1eb\U0001f1f7" , "vf":"\U0001f1f5\U0001f1f1"},
                        {"id":"5",  "local" : "Japón"      , "visitor" : "Croacia", "lf": "\U0001f1ef\U0001f1f5" , "vf":"\U0001f1ed\U0001f1f7"},
                        {"id":"6",  "local" : "Brasil"  , "visitor" : "Corea", "lf": "\U0001f1e7\U0001f1f7" , "vf":"\U0001f1f0\U0001f1f7"},
                        {"id":"7",  "local" : "Marruecos"    , "visitor" : "España", "lf": "\U0001f1f2\U0001f1e6" , "vf":"\U0001f1ea\U0001f1f8"},
                        {"id":"8",  "local" : "Portugal"  , "visitor" : "Suiza", "lf": "\U0001f1f5\U0001f1f9" , "vf":""},
        ]

    cuartos = [         {"id":"9",   "local" : "1"      , "visitor" : "2"},
                        {"id":"10",  "local" : "3"      , "visitor" : "4"},
                        {"id":"11",  "local" : "5"      , "visitor" : "6"},
                        {"id":"12",  "local" : "7"      , "visitor" : "8"},
    ] 

    semis = [           {"id":"13",   "local" : "9"      , "visitor" : "11"},
                        {"id":"14",   "local" : "10"    , "visitor" : "12"},
    ] 

    final = [           {"id":"15",   "local": "13"      , "visitor" : "14"},
                        {"id":"16",  "local" : "13"    , "visitor" : "14"},
    ] 

    if request.method == "POST":
        KOMatch.objects.filter(user_id=request.user.id).delete()
        for x in octavos:
            punt = 1
            if int(x["id"]) <=  2:
                punt = 0 
            local_score=request.POST.get("local"+x["id"])
            visitor_score=request.POST.get("visitor"+x["id"])
            local=x["local"] 
            visitor = x["visitor"]
            pen = 0 
            if local_score == visitor_score:  
                pen = request.POST.get("radio"+x["id"])
            if local_score>visitor_score or pen=="1":
                qual = local
            elif local_score<visitor_score or pen=="2":
                qual = visitor
            game = KOMatch.objects.create(
                local=local ,
                local_score=local_score,
                visitor = visitor,
                visitor_score=visitor_score,
                user_id = request.user.id   , 
                match_number = x["id"],
                round = 1, 
                qualified = qual ,
                punteable = punt 
                )
        oct =   KOMatch.objects.filter(user_id=request.user.id, round =1 )
        for x in cuartos:
            local_score=request.POST.get("local"+x["id"])
            visitor_score=request.POST.get("visitor"+x["id"])
            local=oct.get(match_number=x["local"]).qualified
            visitor =oct.get(match_number=x["visitor"]).qualified
            pen = 0 
            if local_score == visitor_score:  
                pen = request.POST.get("radio"+x["id"])
            if local_score>visitor_score or pen=="1":
                qual = local
            elif local_score<visitor_score or pen=="2":
                qual = visitor
            game = KOMatch.objects.create(
                local=local ,
                local_score=local_score,
                visitor = visitor,
                visitor_score=visitor_score,
                user_id = request.user.id   , 
                match_number = x["id"],
                round = 2, 
                qualified = qual 
                )


        cua =   KOMatch.objects.filter(user_id=request.user.id, round =2 )
        for x in semis:
            local_score=request.POST.get("local"+x["id"])
            visitor_score=request.POST.get("visitor"+x["id"])
            local=cua.get(match_number=x["local"]).qualified
            visitor =cua.get(match_number=x["visitor"]).qualified
            pen = 0 
            if local_score == visitor_score:  
                pen = request.POST.get("radio"+x["id"])
            if local_score>visitor_score or pen=="1":
                qual = local
                loos = visitor
            elif local_score<visitor_score or pen=="2":
                qual = visitor
                loos = local
            game = KOMatch.objects.create(
                local=local ,
                local_score=local_score,
                visitor = visitor,
                visitor_score=visitor_score,
                user_id = request.user.id   , 
                match_number = x["id"],
                round = 3, 
                qualified = qual ,
                looser = loos
                )

        sem =   KOMatch.objects.filter(user_id=request.user.id, round =3 )
        for x in final:
            if x["id"] == "15":
                local=sem.get(match_number=x["local"]).looser
                visitor =sem.get(match_number=x["visitor"]).looser
            if x["id"] == "16":
                local=sem.get(match_number=x["local"]).qualified
                visitor =sem.get(match_number=x["visitor"]).qualified  
            
            local_score=request.POST.get("local"+x["id"])
            visitor_score=request.POST.get("visitor"+x["id"])       
            pen = 0 
            if local_score == visitor_score:  
                pen = request.POST.get("radio"+x["id"])
            if local_score>visitor_score or pen=="1":
                qual = local
            elif local_score<visitor_score or pen=="2":
                qual = visitor
            game = KOMatch.objects.create(
                local=local ,
                local_score=local_score,
                visitor = visitor,
                visitor_score=visitor_score,
                user_id = request.user.id   , 
                match_number = x["id"],
                round = 4, 
                qualified = qual 
                )
        
        
        
        
        
        return redirect('/desk/')









    
    context  = {"octavos" : octavos,
                "cuartos" : cuartos, 
                "semis":     semis, 
                "final" :    final }
    return render(request, 'ko/create.html', context)