from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'date_birth')

admin.site.register(Person, PersonAdmin)