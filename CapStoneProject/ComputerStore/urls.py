from django.urls import path
from . import views

urlpatterns = [

    #------------------------------Product
    path('product/',views.ProductListView.as_view(), name='product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:id>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:id>/delete/',views.ProductDeleteView.as_view(), name='product_delete'),

    #------------------------------Support
    path('support/',views.SupportListView.as_view(), name='support_list'),
    path('support/create/', views.SupportCreateView.as_view(), name='support_create'),
    path('support/<int:id>/delete/',views.SupportDeleteView.as_view(), name='support_delete'),

    #------------------------------Homepage
    path ('',views.homepage,name='homepage'),

    #------------------------------Registation
    path('registation/signup/', views.SignUpView.as_view(), name='signup'),

]
