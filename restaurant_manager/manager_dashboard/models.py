from django.db import models
from django.contrib.auth.models import User



class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

# models.py

from django.db import models

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

# models.py


class StaffMenuItem(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff_member.name} - {self.menu_item.name}"
