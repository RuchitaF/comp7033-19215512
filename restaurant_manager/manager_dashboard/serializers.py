from rest_framework import serializers
from .models import Menu, StaffMember,StaffMenuItem
from staff.forms import forms

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# serializers.py



class StaffMenuItemSerializer(serializers.ModelSerializer):
    staff_member = serializers.PrimaryKeyRelatedField(queryset=StaffMember.objects.all())
    #menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = StaffMenuItem
        fields = ('id', 'staff_member', 'menu_item', 'date_added', 'added_by')
