from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Product, Support

# Register your models here.
admin.site.register(Users, UserAdmin)
admin.site.register(Product)
admin.site.register(Support)
