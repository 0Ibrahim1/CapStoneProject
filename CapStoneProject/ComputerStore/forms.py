from django import forms
from .models import Users, Product, Support


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        error_messages = {
            "username": {
                # "max_length": "Keep it simple."
            }
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user_id','product_id','product_name','description','status','created_at']

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['username','title','description','created_at']