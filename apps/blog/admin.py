from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(Imagenes)
admin.site.register(Ruleta)
admin.site.register(Video)
admin.site.register(Blog, BlogAdmin)
