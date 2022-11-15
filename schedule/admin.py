from django.contrib import admin

# Register your models here.
from .models import Match, RealScore, UserScore

class MatchAdmin (admin.ModelAdmin):
    list_display = ["user_id", 'match_number','local','local_score','visitor','visitor_score',]

admin.site.register(Match,MatchAdmin)

class RSAdmin (admin.ModelAdmin):
    list_display = ['id','local_score','visitor_score']

admin.site.register(RealScore,RSAdmin)

class UserScoreAdmin (admin.ModelAdmin):
    list_display = ['user', 'points']

admin.site.register(UserScore,UserScoreAdmin)