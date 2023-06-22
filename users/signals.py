from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User , UserProfile
from cart.models import Cart
@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.slug = instance.username
        profile.save()
        cart = Cart()
        cart.user = instance
        cart.save()