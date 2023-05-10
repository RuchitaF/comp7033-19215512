from django.shortcuts import render
from datetime import datetime

app_name= 'menu',

def weekly_menu(request):
    menu = {
        'Monday': ['Spaghetti', 'Caesar salad', 'Garlic bread'],
        'Tuesday': ['Taco salad', 'Beef burrito', 'Chips and salsa'],
        'Wednesday': ['Chicken alfredo', 'Caprese salad', 'Breadsticks'],
        'Thursday': ['Sushi rolls', 'Miso soup', 'Edamame'],
        'Friday': ['Fish and chips', 'Coleslaw', 'Tartar sauce'],
        'Saturday': ['Steak', 'Baked potato', 'Green beans'],
        'Sunday': ['Roast beef', 'Mashed potatoes', 'Gravy']
    }

    context = {'menu': menu}
    return render(request, 'menu/weekly_menu.html', context)


def daily_menu(request):
    menu = {
        'Monday': ['Spaghetti', 'Caesar salad', 'Garlic bread'],
        'Tuesday': ['Taco salad', 'Beef burrito', 'Chips and salsa'],
        'Wednesday': ['Chicken alfredo', 'Caprese salad', 'Breadsticks'],
        'Thursday': ['Sushi rolls', 'Miso soup', 'Edamame'],
        'Friday': ['Fish and chips', 'Coleslaw', 'Tartar sauce'],
        'Saturday': ['Steak', 'Baked potato', 'Green beans'],
        'Sunday': ['Roast beef', 'Mashed potatoes', 'Gravy']
    }
    # Get the selected day from the request parameters
    day = request.GET.get('day', datetime.today().strftime('%A'))

    # Get the daily menu for the selected day
    daily_items = menu.get(day, [])

    # Render the daily_menu.html template with the daily menu items
    return render(request, 'menu/daily_menu.html', {'day': day, 'daily_items': daily_items})