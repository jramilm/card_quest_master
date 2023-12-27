import json
from .models import PokemonCard, Trainer
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TrainerForm
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15


class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')


class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')


class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemoncards.html"
    json_file_path = 'data/pokemon_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context

    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])
