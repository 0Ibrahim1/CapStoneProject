from django import forms 
from .models import Users, Product, Support
from django.contrib.auth.forms import UserCreationForm
#for image size
from .validate import check_file_size_10mb
#for custom user
from django.contrib.auth import get_user_model

#------------------------------to get Custom user
CustomeUser = get_user_model()

#------------------------------UsersForm
class UsersForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['username']
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
        fields = ['product_name','description','uploaded_image','status']

#------------------------------SupportForm
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['title','description','uploaded_image']
        error_messages = {
            "title": {
                "max_length": "Small and To-Point."
            }
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['uploaded_image'].validators.append(check_file_size_10mb)