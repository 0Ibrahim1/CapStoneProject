from django import forms
from .models import Users, ComputerStore, Roles, Support


class UsersForm(forms.ModelForm):
    class Meta:
        model = ComputerStore
        fields = ['username', 'password']
        error_messages = {
            "username": {
                # "max_length": "Keep it simple."
            }
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = ComputerStore
        fields = ['user_id','product_id','product_name','description','status','created_at']

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['username','title','description','created_at']