from django.db import models

class Users (models.Model):
  logged = models.BooleanField (null=False, default=False)
  user_id= models.IntegerField (null=False, unique=True)
  username= models.CharField (max_length=30,primary_key=True, unique=True)
  password= models.CharField (max_length=255)
  premission_level= models.CharField (null=False, default= "basic_user")
  cart= models.TextField 
  created_at= models.TimeField (null=False)
  def __str__(self):
    return self.username

class ComputerStore (models.Model):
  logged = models.BooleanField (null=False, default=False)
  user_id= models.IntegerField (null=False, unique=True)
  premission_level= models.CharField (null=False, default= "basic_user")
  product_id= models.IntegerField (unique=True, null=False) 
  product_name= models.CharField (primary_key=True)
  description= models.TextField 
  status = models.CharField (null=False, default= "in Stock")
  created_at= models.TimeField (null=False)
  def __str__(self):
    return self.user_id

class Support (models.Model):
  logged = models.BooleanField (null=False, default=False)
  user_id= models.IntegerField (null=False, unique=True)
  username= models.CharField (max_length=30,primary_key=True, unique=True)
  premission_level= models.CharField (null=False, default= "basic_user")
  title=models.CharField (max_length=100,null=False)
  description= models.TextField
  created_at= models.TimeField (null=False)
  def __str__(self):
    return self.username

class Roles(models.TextChoices):
  BASICUSER = "basic_user","basic_user"
  SUPERUSER = "super_user","super_user"
  STAFF = "staff","staff"
  MANAGER = "manager", "manager"
role = models.CharField(max_length=30,choices=Roles.choices, default=Roles.BASICUSER)
