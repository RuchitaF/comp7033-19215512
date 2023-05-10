from rest_framework import viewsets
from menus.models import Menu
from menus.serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
