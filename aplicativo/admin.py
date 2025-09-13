from django.contrib import admin
from .models import Fruta

class FrutaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'familia', 'genero']

admin.site.register(Fruta, FrutaAdmin)