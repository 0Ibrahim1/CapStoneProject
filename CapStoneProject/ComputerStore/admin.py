from django.contrib import admin
from .models import Users, ComputerStore

# Register your models here.
admin.site.register(Users)
admin.site.register(ComputerStore)