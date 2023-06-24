from django.urls import path
from . import views
urlpatterns = [
    path('',views.GameView.as_view(), name='home'),
    path('404/',views.defualt_404_page, name='404'),
    path('game/<slug:slug>',views.GameDetailView.as_view(),name='gamePage'),
    path('character/<slug:slug>',views.CharacterDetailView.as_view(),name='char'),
    path("search/",views.Search.as_view(),name="search"),
    path("browse/",views.BrowseView.as_view(),name='browse' )
]
