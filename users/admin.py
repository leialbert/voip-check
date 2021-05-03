from django.contrib import admin

# Register your models here.
from .models import User



class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','mobilephone','update_time']
    search_fields = ['username','mobilephone']

admin.site.register(User, UserAdmin)