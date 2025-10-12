from django.db import models
from django.contrib.auth.models import AbstractUser

class Users (AbstractUser):
  class Roles(models.TextChoices):
    BASICUSER = "basic_user","basic_user"
    SUPERUSER = "super_user","super_user"
    STAFF = "staff","staff"
    MANAGER = "manager", "manager"
  logged_in = models.BooleanField(null=False, default=False)
  user_id= models.IntegerField(null=False, unique=True, default=0)
  user_names= models.CharField(max_length=30, primary_key=True, unique=True)
  premission_level = models.CharField(null=False, max_length=30, choices=Roles.choices, default=Roles.BASICUSER)
  password= models.CharField(max_length=255, null=False)
  cart= models.TextField 
  created_at= models.TextField(null=False)
  def __str__(self):
    return self.user_names

class Product (models.Model):
  users_logged_in = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='logged_in',)
  users_user_id= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_id')
  users_user_names= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_names')
  users_premission_level= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='premission_level')
  product_id= models.IntegerField(unique=True, null=False) 
  product_name= models.CharField(primary_key=True)
  description= models.TextField ()
  status = models.CharField(null=False, default= "in Stock")
  created_at= models.CharField(null=False, default='n/a')
  def __str__(self):
    return self.users_user_id

class Support (models.Model):
  users_logged_in = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='logged_in')
  users_user_id= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_id')
  users_user_names= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_names')
  users_premission_level= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='premission_level')
  support_id = models.TextField(null=False)
  title=models.CharField(max_length=100,null=False)
  description= models.TextField()
  created_at= models.TextField(null=False)
  def __str__(self):
    return self.users_user_names


