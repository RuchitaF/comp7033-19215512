from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('weekly-menu/', views.weekly_menu, name='weekly_menu'),
    path('daily-menu/', views.daily_menu, name='daily_menu'),
]
