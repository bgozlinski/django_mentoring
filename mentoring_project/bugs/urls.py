from django.urls import path
from .views import GetAllBugs, bugs_view

urlpatterns = [
    path('all/', GetAllBugs.as_view(), name='get_all_bugs'),
    path('', bugs_view, name='bugs_view'),
]
