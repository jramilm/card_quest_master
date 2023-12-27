from django.contrib import admin
from django.urls import path
from cardquest.views import HomePageView, TrainerList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
]