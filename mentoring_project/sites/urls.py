from django.urls import path
from .views import FavoriteSitesView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favorite/', FavoriteSitesView.as_view(), name='favorite-sites'),
]
