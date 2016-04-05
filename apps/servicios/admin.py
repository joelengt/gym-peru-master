from django.contrib import admin
from .models import *


class EntrenarAdmin(admin.ModelAdmin):
    exclude = ('titulo',)

class NutricionAdmin(admin.ModelAdmin):
    exclude = ('titulo',)

class ConvenioAdmin(admin.ModelAdmin):
    exclude = ('titulo',)



admin.site.register(Entrenar,EntrenarAdmin)
admin.site.register(Nutricion,NutricionAdmin)
admin.site.register(Convenio,ConvenioAdmin)
admin.site.register(Servicio)
