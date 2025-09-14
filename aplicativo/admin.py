from django.contrib import admin
from .models import Fruta, Nutricao

class FrutaAdmin(admin.ModelAdmin):
    list_display = ['name', 'family', 'genus']

class NutricaoAdmin(admin.ModelAdmin):
    list_display = ['calories', 'fat', 'sugar', 'carbohydrates', 'protein']

admin.site.register(Fruta, FrutaAdmin)
admin.site.register(Nutricao, NutricaoAdmin)