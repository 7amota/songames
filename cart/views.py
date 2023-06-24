from typing import Any, Dict
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cart, CartItem, WishList
from users.models import User
from games.models import Game
from django.contrib import messages
class CartView(LoginRequiredMixin,generic.View):
    template_name = 'pages/cart.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        cart = Cart.objects.select_related("user").get(user=request.user)
        cart_item = CartItem.objects.select_related("cart").filter(cart=cart,check_out=False)
        check_cart_item = CartItem.objects.select_related("cart").filter(cart=cart,check_out=False).exists()
        context = {'cart':cart,"cart_item":cart_item,"check_out":check_cart_item}
        return render(request, self.template_name, context=context)
    def post(self,request):
       cart = Cart.objects.select_related("user").get(user=request.user)
       cart_item = CartItem.objects.select_related("cart","game").filter(cart=cart,check_out=False)
       if 'cancle' in request.POST:
        id = request.POST.get('id')
        itemm = cart_item.get(id=id)
        itemm.delete()
        return self.get(request)
           
       if "plus" in request.POST:
        id = request.POST.get('id')
        game = Game.objects.get(id=id)
        cart= cart_item.get(game=game)
        cart.quantity += 1
        cart.save()
        return self.get(request)
       if "minus" in request.POST:
           id = request.POST.get('id')
           game = Game.objects.get(id=id)
           cart= cart_item.get(game=game)
           cart.quantity -= 1
           cart.save()
           return self.get(request)

       if "password" in request.POST:
            password = request.POST['password']
            if request.user.check_password(password):
                for item in cart_item:
                    item.check_out = True
                    item.save()
                messages.success(request,"check out done successfully .")
                return self.get(request)
       messages.error(request,"the password is not correct please try again .")
       return self.get(request)

class UserGames(LoginRequiredMixin,generic.ListView):
    model = CartItem
    template_name = 'pages/mygames.html'
    def get(self,request):
        cart = get_object_or_404(Cart,user=request.user)
        cart_item = CartItem.objects.select_related("cart").filter(cart=cart,check_out=True)
        context = {"item":cart_item}
        return render(request,self.template_name,context=context)

class WishListView(LoginRequiredMixin,generic.ListView):
    model = WishList
    template_name = 'pages/wishlist.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        wish = WishList.objects.select_related("user","game").filter(user=request.user)
        context = {'item':wish}
        return render(request, self.template_name,context=context)