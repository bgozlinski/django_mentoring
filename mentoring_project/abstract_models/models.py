from django.db import models

class ElectronicDevice(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    production_date = models.DateField()

    class Meta:
        abstract = True


class Smartphone(ElectronicDevice):
    screen_size = models.FloatField()
    battery_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=50)


class Laptop(ElectronicDevice):
    processor = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.IntegerField()