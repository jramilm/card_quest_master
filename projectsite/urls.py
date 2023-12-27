from django.contrib import admin
from django.urls import path
from cardquest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemoncard_list', views.PokemonCardListView.as_view(), name='pokemoncard-list'),
    path('pokemoncard_list/add', views.PokemonCreateView.as_view(), name='pokemon-add'),
    path('pokemoncard_list/<pk>', views.PokemonUpdateView.as_view(), name='pokemon-update'),
    path('pokemoncard_list/<pk>/delete', views.PokemonDeleteView.as_view(), name='pokemon-delete'),
    path('collection_list', views.CollectionList.as_view(), name='collection-list'),
    path('collection_list/add', views.CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', views.CollectionUpdateView.as_view(), name='collection-update'),
    path('collection_list/<pk>/delete', views.CollectionDeleteView.as_view(), name='collection-delete'),
]