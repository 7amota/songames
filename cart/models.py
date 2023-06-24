from django.db import models

from users.models import User
from games.models import Game
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='cart_user')
    
    def __str__(self) -> str:
        return self.user.username



class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name='caaart')
    quantity = models.IntegerField(null=True, blank=True, default=1)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT,related_name="gammme")
    check_out = models.BooleanField(null=True, blank=True, default=False)
    def __str__(self) -> str:
        return f"{self.cart.user.username}, {self.game.name}"

    class Meta:
        unique_together = ('game','cart')
        index_together = ('game','cart')
class WishList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    game = models.ForeignKey(Game,on_delete=models.CASCADE, related_name='game')
    class Meta:
        unique_together = ("user","game")
        index_together = ("user","game")
    def __str__(self):
        return f"{self.user.username} - f{self.game.name}"
    