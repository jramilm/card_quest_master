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
]