from django.contrib import admin
from .models import PokemonCard, Trainer, Collection


class PokemonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PokemonCard._meta.fields]
    search_fields = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Collection._meta.fields]
    search_fields = ('trainer', 'card')


class TrainerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Trainer._meta.fields]
    search_fields = ('name',)


admin.site.register(PokemonCard, PokemonAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Trainer, TrainerAdmin)