from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Users, Support
from .forms import UsersForm, ProductForm,SupportForm
# auth imports
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#------------------------------Homepage
def homepage(request):
    return render(request, 'homepage.html')

#------------------------------Custom Users
CustomUser = get_user_model()
class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.permission_level == 'manager'
    
class ManagerOrStaffAccessMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        # Check if the user is EITHER a manager OR staff
        is_manager = user.permission_level == 'manager'
        is_staff = user.permission_level =='staff'
        return is_manager or is_staff

class ManagerOrStaffOrPremiumAccessMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        # Check if the user is EITHER a manager OR staff OR premium_user
        is_manager = user.permission_level == 'manager'
        is_staff = user.permission_level =='staff'
        is_premium = user.permission_level == 'premium_user'
        return is_manager or is_staff or is_premium
    
#------------------------------Singup
class SignUpView(CreateView):
    model = get_user_model()
    form_class= UsersForm
    success_url = '/auth/login'
    template_name = 'registration/sign-up.html'

#------------------------------CRUD for Prodcut
class ProductListView(ListView):
    model = Product
    template_name='product/all-product.html'
    context_object_name = 'all_product'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-details.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

class ProductCreateView(LoginRequiredMixin, ManagerOrStaffAccessMixin, CreateView):
    model=Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    success_url= reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, ManagerOrStaffAccessMixin, UpdateView):
    model= Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, ManagerOrStaffAccessMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

#------------------------------CRUD for Support
class SupportListView(LoginRequiredMixin, ManagerOrStaffAccessMixin, ListView):
    model= Support
    template_name='support/suport-list.html'
    context_object_name = 'support'

def support_list(request):
    support = Support.objects.all()
    return render(request, 'support/support-list.html',{'support':support})

class SupportCreateView(LoginRequiredMixin, ManagerOrStaffOrPremiumAccessMixin, CreateView):
    model = Support
    template_name = 'Support/support-form.html'
    form_class = SupportForm
    success_url=reverse_lazy('book_list')

class SupportUpdateView(LoginRequiredMixin, ManagerOrStaffAccessMixin, UpdateView):
    model = Support
    template_name = 'support/support-form.html'
    form_class = SupportForm
    success_url = reverse_lazy('support_list')

class SupportDeleteView(LoginRequiredMixin, ManagerRequiredMixin, DeleteView):
    model = Support
    success_url = reverse_lazy('support_delete')

