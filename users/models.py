from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    choices_gender = (
        ("male","male"),
        ("female","female")
    )
    email = models.EmailField(max_length=80, unique=True)
    image = models.ImageField(upload_to='Photos/%y/%m/%d',null=True , blank=True)
    username = models.CharField(max_length=45)
    phoneNumber = models.IntegerField(null=True , blank=True)
    dateBirth = models.DateField(null=True , blank=True)
    location = models.TextField(null=True , blank=True)
    gender = models.TextField(null=True , blank=True , choices=choices_gender)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]