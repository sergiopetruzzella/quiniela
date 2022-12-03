from django.contrib import admin

# Register your models here.
from .models import KOMatch , KORealScore

class KOMatchAdmin (admin.ModelAdmin):
    list_display = ["user_id", 'match_number','local','local_score','visitor','visitor_score','round', 'qualified', 'looser', 'punteable']

admin.site.register(KOMatch,KOMatchAdmin)

class KORealScoreAdmin (admin.ModelAdmin):
    list_display = ["id",'local','local_score','visitor','visitor_score','round', 'qualified', 'looser']

admin.site.register(KORealScore,KORealScoreAdmin)

