from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
