from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group


class GroupAdmin (admin.ModelAdmin):
    list_display = ["name", 'user','users']

admin.site.register(Group,GroupAdmin)
