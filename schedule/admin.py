from django.contrib import admin

# Register your models here.
from .models import Match

class MatchAdmin (admin.ModelAdmin):
    list_display = ["user_id", 'match_number','local','local_score','visitor','visitor_score',]

admin.site.register(Match,MatchAdmin)