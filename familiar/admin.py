from django.contrib import admin

from .models import Person

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','genero','edad','correo','fecha')

admin.site.register(Person, PersonaAdmin)
