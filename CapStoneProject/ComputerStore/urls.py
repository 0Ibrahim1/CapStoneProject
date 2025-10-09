from django.urls import path
from . import views

urlpatterns = [
    # -----------------------------------------------------------------Logged in 
    #Product
    path('logged/product/create/', views.ProductCreateView.as_view(), name='prodcut_create'),
    path('logged/product/<int:id>/edit', views.ProductUpdateView.as_view(),  name='product_edit'),
    path('logged/product/<int:id>/delete/',views.ProductDeleteView.as_view(), name='product_delete'),

    #Support
    path('logged/support/create/',views.SupportCreateView.as_view(), name='support_create'),
    path('logged/support/<int:id>/delete/',views.SupportDeleteView.as_view(), name='support_delete'),


    # ----------------------------------------------------------------Not logged in
    #Product
    path('not-logged/product/',views.ProductListView.as_view(), name='product_list'),
    path('not-logged/product/<int:id>/', views.ProductDetailView.as_view(),  name='product_details'),

    #Homepage
    path ('',views.homepage,name='homepage'),

    # ----------------------------------------------------------------Registation
    path('registation/signup/', views.SignUpView.as_view(), name='signup'),

]
