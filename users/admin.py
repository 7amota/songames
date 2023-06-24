from django.contrib import admin
from . import models
# Register your models here.
admin.site.site_title = "CodeClub"
admin.site.site_header = "CodeClub"
admin.site.index_title = "CodeClub Administration"
admin.site.register(models.User)
admin.site.register(models.UserProfile)