from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list_view, name='product-list'),
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/<str:category_id>/', views.category_product_list_view, name='category-product-list'),
]
