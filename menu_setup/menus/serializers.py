from rest_framework import serializers
from menus.models import Menu, Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        restaurant_data = validated_data.pop('restaurant')
        restaurant = Restaurant.objects.create(**restaurant_data)
        menu = Menu.objects.create(restaurant=restaurant, **validated_data)
        return menu

    def update(self, instance, validated_data):
        restaurant_data = validated_data.pop('restaurant')
        restaurant_serializer = RestaurantSerializer(instance.restaurant, data=restaurant_data)
        restaurant_serializer.is_valid(raise_exception=True)
        restaurant_serializer.save()

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        return instance
