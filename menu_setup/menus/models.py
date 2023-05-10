from django.db import models

class Restaurant(models.Model):
    restaurant_id= models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)
    tables = models.PositiveIntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
