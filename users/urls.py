from django.urls import path,include
from . import views
urlpatterns = [
    path('login-register/',views.LoginAndRegister.as_view(), name='login-register'),
    path('profile/',views.UserProfileView.as_view(), name='profile')
]
