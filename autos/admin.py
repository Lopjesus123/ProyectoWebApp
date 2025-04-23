from django.contrib import admin
from .models import Marca, Auto

class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class AutoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Auto, AutoAdmin)
