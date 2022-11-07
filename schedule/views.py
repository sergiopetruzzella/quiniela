from django.shortcuts import render
from .models import Schedule, Match


# Create your views here.
def schedule_create_view(request):
    
    match_schedule = [{"id":"1",  "local" : "Catar"   , "visitor" : "Ecuador"},
                      {"id":"2",  "local" : "Senegal" , "visitor" : "Holanda"},
                      {"id":"3",  "local" : "Catar"   , "visitor" : "Senegal"},
                      {"id":"4",  "local" : "Holanda" , "visitor" : "Ecuador"},
                      {"id":"5",  "local" : "Ecuador" , "visitor" : "Senegal"},
                      {"id":"6",  "local" : "Holanda" , "visitor" : "Catar"  },
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
        render(request, 'schedule/create.html', {})

    context = {"list" :  match_schedule }
    return  render(request, 'schedule/create.html', context)

    