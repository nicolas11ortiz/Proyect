from django.contrib import admin

# Register your models here.

from . models import Juego, Desarrolladora, Genre, Plataforma

admin.site.register(Juego)
admin.site.register(Desarrolladora)
admin.site.register(Genre)
admin.site.register(Plataforma)


