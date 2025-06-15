from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    basket = models.OneToOneField('baskets.Basket', on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='customer_profile')

    def __str__(self):
        return self.name