from django.db import models
from django.contrib.auth.models import AbstractUser

#------------------------------Users Model with custom user
class Users (AbstractUser):
  class Roles(models.TextChoices):
    BASICUSER = "basic_user", "Basic User"
    PREMIUMUSER = "premium_user", "Premium User"
    STAFF = "staff", "Staff"
    MANAGER = "manager", "Manager"
  permission_level = models.CharField(null=False, max_length=30, choices=Roles.choices, default=Roles.BASICUSER)
  cart= models.TextField(blank=True, null=True) 
  def __str__(self):
    return self.username

#------------------------------Product model 
class Product (models.Model):
  user_id= models.ForeignKey(Users, on_delete=models.CASCADE, related_name="product_user",null=True)
  product_image=models.ImageField()
  product_name= models.CharField(max_length=255, null=False, unique=True)
  description= models.TextField ()
  uploaded_image= models.ImageField(upload_to='ComputerStore/Product_image/%Y/%M/%D',null=True,blank=True,db_index=True,verbose_name='Product image')
  status = models.CharField(null=False, default= "in Stock")
  created_at= models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.product_name

#------------------------------Support model
class Support (models.Model):
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="support_user",null=True)
  title=models.CharField(max_length=150,null=False)
  description= models.TextField()
  uploaded_image= models.ImageField(upload_to='ComputerStore/Uploaded-images/%Y/%M/%D',null=True,blank=True,db_index=True,verbose_name='Uploaded image')
  created_at= models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title


