from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Users, Support
from .forms import UsersForm, ProductForm,SupportForm
# auth imports
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.mixins import LoginRequiredMixin



def homepage(request):
    return render(request, 'homepage.html')

class CustomUser(AbstractUser):
    pass

# CRUD for Prodcut
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name='product/all-product.html'
    context_object_name = 'all_product'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-details.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model=Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    success_url= reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model= Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

# Singup
class SignUpView(CreateView):
    model = Users
    form_class= UserCreationForm
    success_url = '/auth/login'
    template_name = 'registration/sign-up.html'

# CRUD for Support

class SupportistView(ListView):
    model= Support
    template_name='support/suport-list.html'
    context_object_name = 'support'

def support_list(request):
    support = Support.objects.all()
    return render(request, 'support/support-list.html',{'support':support})


class SupportCreateView(CreateView):
    model = Support
    template_name = 'Support/support-form.html'
    form_class = SupportForm
    success_url=reverse_lazy('book_list')


class SupportUpdateView(UpdateView):
    model = Support
    template_name = 'support/support-form.html'
    form_class = SupportForm
    success_url = reverse_lazy('support_list')

class SupportDeleteView(DeleteView):
    model = Support
    success_url = reverse_lazy('support_list')