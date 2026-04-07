from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_route, name='add_route'),  #frontpage shows add_route
    path('longest/',views.longest_route,name='longest_route'),  #to get longest route
    path('search/',views.search_node,name='search_node'),
]