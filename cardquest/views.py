from django.shortcuts import render
from .models import Pokemoncard
    
# Create your views here.
class HomePageView(ListView):
    model = Pokemoncard
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    