from django.contrib import admin
from .models import Users, Product, Support

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Support)