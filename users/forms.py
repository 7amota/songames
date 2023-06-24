from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .validators import passwdvalidate
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':"form-control rounded-5 p-2"}),
            'password': forms.PasswordInput(attrs={'class':"form-control rounded-5 p-2"})
        }
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control rounded-5 p-2 mb-3"}), validators=[passwdvalidate])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control rounded-5 p-2 mb-3"}),validators=[passwdvalidate])
    class Meta:
        model = User
        fields = ['email','username','dateBirth', 'gender','password1','password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class':"form-control rounded-5 p-2"}),
            'username': forms.TextInput(attrs={'class':"form-control rounded-5 p-2"}),
            'dateBirth': forms.DateInput(attrs={'class':"form-control rounded-5 mb-3 p-2 dateInput", 'type':'date'}),
            'gender': forms.Select(attrs={'class':"form-control rounded-5 p-2"}),
            'password1': forms.PasswordInput(attrs={'class':"form-control rounded-5 p-2 mb-3"}, ),
            'password2': forms.PasswordInput(attrs={'class':"form-control rounded-5 p-2 mb-3"}),

        }

class UpdateForm(forms.ModelForm):
    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"val":"Change Image",'class':"custom-file-input position-relative form-control pb-4"}))
    password1 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={"class": "form-control bg-border-gradien rounded-5 p-2 mb-3"}))
    password2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={"class": "form-control bg-border-gradien rounded-5 p-2 mb-3"}))
    class Meta:
        model = User
        fields = ['email','username','dateBirth', 'gender','password1','password2',"image"]
        widgets = {
            'email': forms.EmailInput(attrs={'class':"form-control bg-border-gradien rounded-5 mb-3 p-2"}),
            'username': forms.TextInput(attrs={'class':"form-control bg-border-gradien rounded-5 mb-3 p-2"}),
            'dateBirth': forms.DateInput(attrs={'class':"form-control bg-border-gradien rounded-5 mb-3 p-2", 'type':'date'}),
            'gender': forms.Select(attrs={'class':"form-control bg-border-gradien rounded-5 p-2 pointer"}),
            'password1': forms.PasswordInput(attrs={'class':"form-control rounded-5 p-2 mb-3"}),
            'password2': forms.PasswordInput(attrs={'class':"form-control rounded-5 p-2 mb-3"}),
            "image":forms.FileInput(attrs={"val":"Change Image",'class':"custom-file-input position-relative form-control pb-4"})
        }
    

# class MyPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(
#         label='Old Password',
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
#     )