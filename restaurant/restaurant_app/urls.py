from django.urls import path
from .views import get_restaurants_with_menu_items

urlpatterns = [
    path('get-restaurants-with-menu-items', get_restaurants_with_menu_items, name='get-restaurants-with-menu-items'),
]
