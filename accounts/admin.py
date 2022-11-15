from django.contrib import admin
from .models import UserContact

# Register your models here.
class UserContactAdmin (admin.ModelAdmin):
    list_display = ["user","instagram", "phone_number" ]

admin.site.register(UserContact,UserContactAdmin)