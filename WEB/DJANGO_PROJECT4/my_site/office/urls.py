from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_players, name='list_players')
] 