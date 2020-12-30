from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

# Con la finalidad de poder hacer uso de nuestros "modelos" debemos registrarlos en "admin.py"
admin.site.register(Project, ProjectAdmin) #admin.site.register(<nombre_modelo>, <configuración_extendida>).
# La configuración extendida es opcional. Para este caso, hacemos uso de la configuración extendida para que
# Django nos muestre los campos "created" y "updated".
