from django.urls import path
from . import views

urlpatterns = [

    #Product
    path('/product/create/', views.ProductCreateView.as_view(), name='prodcut_create'),
    path('/product/<int:id>/edit', views.ProductUpdateView.as_view(),  name='product_edit'),
    path('/product/<int:id>/delete/',views.ProductDeleteView.as_view(), name='product_delete'),

    #Support
    path('/support/create/',views.SupportCreateView.as_view(), name='support_create'),
    path('/support/<int:id>/delete/',views.SupportDeleteView.as_view(), name='support_delete'),

    #Homepage
    path ('',views.homepage,name='homepage'),

    # ----------------------------------------------------------------Registation
    path('registation/signup/', views.SignUpView.as_view(), name='signup'),

]
