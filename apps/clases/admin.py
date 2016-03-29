from django.contrib import admin
from .models import *


class DiaAdmin(admin.ModelAdmin):
    filter_horizontal = ('horas',)


admin.site.register(Horas)
admin.site.register(Aerobicos)
admin.site.register(BestCyclng)
admin.site.register(Clases)
admin.site.register(DeportesDeContacto)
admin.site.register(Dia)
admin.site.register(Horario)
admin.site.register(Talleres)
