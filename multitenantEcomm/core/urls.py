from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    # Home
    path('', views.index, name='index'),
    
    # Products
    path('products/', views.product_list_view, name='product-list'),
    path('product/<str:product_id>/', views.product_detail_view, name='product-detail'),
    
    # Categories 
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/<str:category_id>/', views.category_product_list_view, name='category-product-list'),
]
