from django import forms 
from .models import Users, Product, Support
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

#------------------------------to get Custom user
Users = get_user_model()

#------------------------------UsersForm
class UsersForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['username', 'password']
        Req = {
            'username':{
                'required':True,
                'error_messages' : {
                'username': "Keep it simple.",
                }
            }
        }

#------------------------------ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','description','status']

#------------------------------SupportForm
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['title','description']
        error_messages = {
            "title": {
                # "Recommended title": "Small and To-Point."
            }
        }