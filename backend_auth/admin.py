from django.contrib import admin
from django.contrib.auth.admin import  Useradmin
from .model import *

# customize how admin panel will look like after we have created new custom user model 


class CustomUserAdmin(Useradmin):
    list_display=('email','username','phone_number','date_joined','last_joined','is_admin')
    search_fields=('email','username','phone_number')
    readonly_fields=('id','date_joined','last_joined')

#in case you get error define them as blank 
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(CustomUser,CustomUserAdmin)