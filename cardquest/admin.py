from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

# Register your models here.
# admin.site.register(PokemonCard)

class PokemonAdmin(admin.ModelAdmin):
   list_display = ('name', 'rarity')
   search_fields = ('name',)

admin.site.register(PokemonCard)
admin.site.register(Trainer)
admin.site.register(Collection)