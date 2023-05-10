from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.name
