from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .utlis import get_key
from cart.models import Cart, CartItem, WishList

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def defualt_404_page(request, exception):
    return render(request, 'pages/404.html')

class GameView(ListView, View):
    queryset = Game.objects.all()
    context_object_name = 'games'
    template_name = 'pages/index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        game = Game.objects
        context['fgame'] = game.first()
        context['langames'] = game.all()[1:6]
        context['mostviews'] = game.order_by("-views")[:3]
        context['trend'] = game.order_by("trend")[:10]
        context['pop'] = game.order_by("popular")
        context['mostpop'] = game.order_by('-views')[0]
        context['gallery'] = Gallery.objects.all()
        context['character'] = Character.objects.order_by("?")[:6]
        return context
    def post(self,request):
        if request.user.is_authenticated:
            key = get_key(request)
            game = Game.objects.filter(name=key).first()
            wish,create = WishList.objects.get_or_create(user=request.user,game=game)
            if create:
                messages.success(request, "the game added successfully to wishlist .")
                return redirect('home')
            if wish:
                messages.error(request, "the game is already in wishlit .")
                return self.get(request)
            return self.get(request)
        else:
            return redirect('login-register')



class GameDetailView(LoginRequiredMixin,DetailView, View):
    queryset = Game.objects.all()
    context_object_name = 'game'
    template_name = 'pages/game-details.html'
    def post(self,request,slug):
        if "wishList" in request.POST:
            try:
                wish_list = WishList()
                wish_list.user = request.user
                wish_list.game = self.get_object()
                wish_list.save()
                messages.success(request, "The game added successfully to wishlist")
                return render(request, self.template_name, context={"game":self.get_object()})
            except:
                messages.error(request,"The game is already in wishlist")
                return render(request, self.template_name, context={"game":self.get_object()})
        else:
            try:
                cart = Cart.objects.get(user=request.user)
                cart.check_out = False
                cart.save()
                if not cart:
                    cart = Cart.objects.create(user=request.user)
                cartItem = CartItem.objects.create(game=self.get_object(),cart=cart)
                cartItem.save()
                messages.success(request,"the game added successfully to cart")
                return render(request, self.template_name, context={"game":self.get_object()})
            except:
                messages.error(request, "the game is already in cart, or already in your games")
                return render(request, self.template_name, context={"game":self.get_object()})


            
class CharacterDetailView(LoginRequiredMixin,DetailView):
    queryset = Character.objects.all()
    context_object_name = 'char'
    template_name = 'pages/character.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['rgames'] = Game.objects.order_by("?")[:3]
        return context
class Search(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'pages/search.html'
    context_object_name = 'gm'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            textToSearch = request.GET['searchHeader']
            game = Game.objects.filter(name__icontains=textToSearch)
            context = {'game':game}
            return render(request,self.template_name,context=context)
        except:
            cont = {'game':Game.objects.all()}
            return render(request,self.template_name,cont)

class BrowseView(LoginRequiredMixin,ListView,View):
    model = Game
    template_name = 'pages/browse.html'
    context_object_name = "game"
    def get_queryset(self) -> QuerySet[Any]:
        return Game.objects.all()
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context
    def post(self,request):
        context = {'cat':Category.objects.all()}
        key = get_key(request)
        if key == "all":
            return self.get(request)
        elif key == 'free':
            context['game'] = Game.objects.filter(status=1)
            return render(request,self.template_name,context=context)
        elif key == '95':
            context['game'] = Game.objects.filter(price__lte = 95)
            return render(request,self.template_name,context=context)
        elif key == '190':
            context['game'] = Game.objects.filter(price__lte = 190)
            return render(request,self.template_name,context=context)
        elif key == '280':
            context['game'] = Game.objects.filter(price__lte=280)
            return render(request,self.template_name,context=context)
        else:
            query =Game.objects.prefetch_related('categories').filter(categories__title=key)
            context['game'] = query
            return render(request,self.template_name,context=context)