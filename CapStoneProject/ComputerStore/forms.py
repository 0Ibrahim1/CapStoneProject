from django import forms
from .models import Users, Product, Support


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_names', 'password','created_at']
        error_messages = {
            "user_names": {
                # "max_length": "Keep it simple."
            }
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['users_user_names','product_id','product_name','description','status','created_at']

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['users_user_names','title','description','created_at']