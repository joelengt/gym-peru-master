from django.contrib import admin
from .models import *


class DiaAdmin(admin.ModelAdmin):
    filter_horizontal = ('horas',)


class AerobicosAdmin(admin.ModelAdmin):
    exclude = ('titulo',)


class BestCyclingAdmin(admin.ModelAdmin):
    exclude = ('titulo',)


class DeportesDeContactoAdmin(admin.ModelAdmin):
    exclude = ('titulo',)


class TalleresAdmin(admin.ModelAdmin):
    exclude = ('titulo',)


admin.site.register(Horas)
admin.site.register(Aerobicos, AerobicosAdmin)
admin.site.register(BestCyclng, BestCyclingAdmin)
admin.site.register(Clases)
admin.site.register(DeportesDeContacto, DeportesDeContactoAdmin)
admin.site.register(Dia)
admin.site.register(Horario)
admin.site.register(Talleres, TalleresAdmin)
