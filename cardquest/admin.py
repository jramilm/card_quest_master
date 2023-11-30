from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

# Register your models here.
# admin.site.register(PokemonCard)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity')
    search_fields = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'created_at')
    search_fields = ('trainer', 'card')


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)


admin.site.register(PokemonCard, PokemonAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Trainer, TrainerAdmin)