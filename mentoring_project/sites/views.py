from django.shortcuts import render
from django.views.generic import ListView

from .models import Site

def home(request):
     return render(request, 'sites/home.html')

class FavoriteSitesView(ListView):
    model = Site
    template_name = "sites/favorite_sites.html"
    context_object_name = 'sites'