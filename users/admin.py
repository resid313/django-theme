from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

class PersonAdmin(UserAdmin):
    pass

admin.site.register(Person, PersonAdmin)