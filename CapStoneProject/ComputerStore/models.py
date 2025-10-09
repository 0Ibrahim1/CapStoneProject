from django.db import models

class Users (models.Model):
  logged = models.BooleanField (null=False, default=False)
  user_id= models.IntegerField (null=False, unique=True)
  username= models.CharField (max_length=30,primary_key=True, unique=True)
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
