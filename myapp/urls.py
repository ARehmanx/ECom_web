from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('products/', views.product, name='product_page'),
    path('product_detail/<int:item_id>/', views.product_detail, name='product_detail'),
    path('products/<int:id>/', views.product, name='product_page'),
    path('checkout_cart/<int:id>/', views.add_to_cart, name='cart'),
    path('checkout_cart/', views.checkout_cart, name='checkout_cart'),
    path('products/<int:id>/', views.product_category_detail, name='product_category_detail'),
    path('checkout_info/', views.checkout_info, name='checkout_info'),
    path('add_to_order/', views.add_to_order, name='add_to_order'),
    path('checkout_complete/', views.checkout_complete, name='checkout_complete'),
    path('complete_payment/', views.complete_payment, name='complete_payment'),
    path('checkout_complete/', views.last_page, name='order_done'),
    path('mmmm/', views.delete_cart, name='delete_cart'),
    path('nnnnn/', views.delete_order, name='delete_order'),
]
#new_changes