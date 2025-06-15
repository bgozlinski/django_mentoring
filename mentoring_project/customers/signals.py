from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from baskets.models import Basket


@receiver(post_save, sender=Customer)
def create_basket(sender, instance, created, **kwargs):
    if created:
        basket = Basket.objects.create(customer=instance)
        instance.basket = basket
        instance.save(update_fields=['basket'])

