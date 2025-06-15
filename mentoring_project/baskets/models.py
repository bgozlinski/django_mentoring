from django.db import models

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='customer_baskets')
