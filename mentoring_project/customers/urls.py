from django.urls import path
from . import views

urlpatterns = [
    path('', views.produce_consumer, name='produce_customer'),
]