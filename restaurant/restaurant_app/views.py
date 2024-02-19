# restaurant_app/views.py
from django.http import JsonResponse
from .models import Restaurant

def get_restaurants_with_menu_items(request):
    if request.method == 'GET':
        # Retrieve all restaurants with menu items
        restaurants = Restaurant.objects.all()
        serialized_restaurants = [
            {
                'id': restaurant.id,
                'name': restaurant.name,
                'location': restaurant.location,
                'menu_items': [
                    {
                        'id': item.id,
                        'name': item.name,
                        'description': item.description,
                        'price': float(item.price),
                        'rating': float(item.rating)
                    }
                    for item in restaurant.menuitem_set.all()  # Access related menu items
                ]
            }
            for restaurant in restaurants
        ]

        # Create a JSON response
        response_data = {'restaurants': serialized_restaurants}
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
