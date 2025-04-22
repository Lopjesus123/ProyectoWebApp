from django.contrib import admin

from .models import Servicios

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):

    readonly_fields=('created','update')



admin.site.register(Servicios, ServiciosAdmin)

