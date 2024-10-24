# Register your models here.
from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome','especie', 'raca', 'idade',)
    search_fields = ('nome', 'raca')
    list_filter = ('especie',)

admin.site.register(Animal, AnimalAdmin)

