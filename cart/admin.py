from django.contrib import admin
from .models import Cart, CartItem,WishList
admin.site.register(Cart)
admin.site.register(WishList)
admin.site.register(CartItem)