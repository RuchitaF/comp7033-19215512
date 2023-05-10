from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    position = models.CharField(max_length=255)
    salary = models.CharField(max_length=20)

    def __str__(self):
        return self.name
