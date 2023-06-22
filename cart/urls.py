from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.CartView.as_view(), name='cart'),
    path("mygames/",views.UserGames.as_view(),name="mygames"),
    path("wish/",views.WishListView.as_view(),name="wish")
]
