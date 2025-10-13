from django import forms 
from .models import Users, Product, Support

#------------------------------UsersForm
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_names', 'password','created_at']
        Req = {
            'user_names':{
                'required':True,
                'error_messages' : {
                'user_names': "Keep it simple.",
                }
            }
        }

#------------------------------ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user_names','product_id','product_name','description','status','created_at']

#------------------------------SupportForm
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['user_names','title','description','created_at']
        error_messages = {
            "title": {
                # "Recommended title": "Small and To-Point."
            }
        }