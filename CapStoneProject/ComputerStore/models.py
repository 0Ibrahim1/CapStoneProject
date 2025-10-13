from django.db import models
from django.contrib.auth.models import AbstractUser

#------------------------------Users Model with custom user
class Users (AbstractUser):
  class Roles(models.TextChoices):
    BASICUSER = "basic_user"
    PREMIUMUSER = "premium_user"
    STAFF = "staff"
    MANAGER = "manager"
  logged_in = models.BooleanField(null=False, default=False)
  user_id= models.IntegerField(null=False, unique=True, default=0)
  user_names= models.CharField(max_length=30, primary_key=True, unique=True)
  permission_level = models.CharField(null=False, max_length=30, choices=Roles.choices, default=Roles.BASICUSER)
  password= models.CharField(max_length=150, null=False)
  cart= models.TextField 
  created_at= models.TextField(null=False)
  def __str__(self):
    return self.user_names

#------------------------------Product model 
class Product (models.Model):
  logged_in = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='product_logged_in')
  user_id= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='product_user_id')
  user_names= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='product_user_names')
  permission_level= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='product_permission_level')
  product_id= models.IntegerField(unique=True, null=False) 
  product_name= models.CharField(primary_key=True)
  description= models.TextField ()
  status = models.CharField(null=False, default= "in Stock")
  created_at= models.TextField(null=False)
  def __str__(self):
    return self.product_id

#------------------------------Support model
class Support (models.Model):
  logged_in = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='support_logged_in')
  user_id= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='support_user_id')
  user_names= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='support_user_names')
  permission_level= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='support_prerission_level')
  support_id = models.TextField(null=False)
  title=models.CharField(max_length=100,null=False)
  description= models.TextField()
  created_at= models.TextField(null=False)
  def __str__(self):
    return self.title


