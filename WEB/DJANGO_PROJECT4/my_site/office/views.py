from django.shortcuts import render
from . import models
# Create your views here.
def list_players(request):
    
    all_players=models.Player.objects.all()
    context_list = {'players':all_players}
    return render(request, 'office/list.html', context=context_list)