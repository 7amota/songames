from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, FormView, View, DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from cart.models import WishList
from .forms import *
from .models import UserProfile
from .utils import *
class LoginAndRegister(View):
    template_name = 'pages/login-register.html'
    form_class = LoginForm()
    from_class2 = RegisterForm()
    def get(self,request):
        return render(request,template_name=self.template_name ,context={
            'login':self.form_class,
            'register':self.from_class2
        })
    def post(self,request):
        if "login" in request.POST:
            form = LoginForm()
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request , user)
                return redirect("home")
            else:
                messages.error(request,"Please check the email and password and try again .")
                return render(request, template_name=self.template_name,context={"login":form,'register':self.from_class2,})
        
        if "register" in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                print(1)
                user = form.save()
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect("home")
            messages.error(request,"please check your password and be sure it is more than 8 letters, and the email and password is not similar")
            return render(request,template_name=self.template_name,context={"login":self.form_class,'register':self.from_class2} )
            
class UserProfileView(LoginRequiredMixin ,View):
    template_name = 'pages/user-profile.html'
    def get(self, request):
        user = request.user
        social= get_socila_accounts(request.user)
        update = UpdateForm(instance=request.user)
        wish = WishList.objects.select_related("user").filter(user=request.user).count()
        context = {
            'update':update,
            'user':user,
            "wishNum":wish,
            "social":social,

        }
        return render(request, template_name=self.template_name,context=context )
    def post(self,request):
        print(request.POST)
        update = UpdateForm(request.POST, request.FILES, instance=request.user)
        if update.is_valid():
                passwd1 = update.cleaned_data['password1']
                passwd2 = update.cleaned_data['password2']
                if passwd1 and passwd2:   
                    if passwd_validate(request=request,user=request.user, passwd1=passwd1, passwd2=passwd2):
                        return render(request=request,template_name= self.template_name, context={'update':update})
                    else:
                        messages.error(request,'password 1 not similar to password 2')
                    return render(request=request,template_name= self.template_name, context={'update':UpdateForm(instance=request.user)})
                update.save()
                messages.success(request,"The user data saved successfully .")
                return render(request=request,template_name= self.template_name, context={'update':update})
        else:
            messages.error(request, "the username or email may used before")
            return render(request,self.template_name,context={'update':UpdateForm(instance=request.user)})


