from django.contrib import admin

# Register your models here.
from .models import User,Whiteip



class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','mobilephone','update_time']
    search_fields = ['username','mobilephone']

class WhiteipAdmin(admin.ModelAdmin):
    list_display = ['user','whiteip']

admin.site.register(User, UserAdmin)
admin.site.register(Whiteip, WhiteipAdmin)