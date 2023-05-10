from django.urls import path, include
from rest_framework import routers
from menus.views import MenuViewSet,RestaurantSerializer

router = routers.DefaultRouter()
router.register(r'menus', MenuViewSet)

app_name = 'menu'

urlpatterns = [
    path('', include(router.urls)),
]
