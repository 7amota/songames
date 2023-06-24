from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator
from users.models import User
from slugify import slugify
class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=True, blank=True)
    details = models.TextField(null=True, blank=True, validators=[MinLengthValidator(100),MaxLengthValidator(150)])
    details2 = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="photos/character/%y/%m/%d",validators=[FileExtensionValidator(['webp','png','jpg','avif','jpeg'])])
    slug = models.SlugField(null=True, blank=True,help_text="NEVER EVER EDIT")
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Character, self).save(*args, **kwargs)
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self) -> str:
        return self.title

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="Photos/gallery/%y/%m/%d",validators=[FileExtensionValidator(['webp','png','jpg','avif','jpeg'])])
    

class Game(models.Model):
    id = models.AutoField(primary_key=True)

    STATUS = (
        (1,"Free"),
        (2,"Paid")
    )
    name = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS,blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    trend = models.BooleanField(blank=True, null=True)
    logo = models.FileField(upload_to='Photos/logo/%y/%m/%d', validators=[FileExtensionValidator(['webp','png','jpg','avif','jpeg'])])
    banner = models.FileField(upload_to='Photos/banner/%y/%m/%d',validators=[FileExtensionValidator(['webp','png','jpg','avif','jpeg'])])
    popular = models.BooleanField(null=True, blank=True)
    bannerLogo = models.FileField(upload_to='Photos/bannerLogo/%y/%m/%d',validators=[FileExtensionValidator(['webp','png','jpg','avif','jpeg'])])
    releaseDate = models.DateField(null=True, blank=True)
    intialRelease = models.DateField(null=True, blank=True)
    platform = models.CharField(null=True, blank=True, max_length=300)
    publisher = models.CharField(null=True, blank=True,max_length=300)
    developer = models.CharField(null=True, blank=True,max_length=300)
    features = models.CharField(null=True, blank=True,max_length=300)
    views = models.IntegerField(blank=True, null=True, help_text="DON`T EDIT")
    character = models.OneToOneField(Character, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(null=True, blank=True,help_text="NEVER EVER EDIT")
    def __str__(self) -> str:
        return self.name
    @property
    def get_price_after_sale(self) ->int:
        if self.discount:
            return self.price - ((self.discount / 100) * self.price )
        return 0
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Game, self).save(*args, **kwargs)
