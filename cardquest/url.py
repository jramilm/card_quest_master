from django.urls import path
from .views import HomePageView, TrainerList
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
]