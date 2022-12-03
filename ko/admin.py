from django.contrib import admin

# Register your models here.
from .models import KOMatch

class KOMatchAdmin (admin.ModelAdmin):
    list_display = ["user_id", 'match_number','local','local_score','visitor','visitor_score','round', 'qualified', 'looser', 'punteable']

admin.site.register(KOMatch,KOMatchAdmin)
