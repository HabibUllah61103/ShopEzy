from django.urls import path
from ShopEzy_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("customer_signup", views.customer_signup, name="customer_signup"),
    path("customer_signin", views.customer_signin, name="customer_signin"),
    path("customer_profile", views.customer_profile, name="customer_profile"),
    path("product_view/<str:customer_id>", views.product_view, name="product_view"),
    path("product_detail/<str:category_name>/<str:customer_id>", views.product_detail, name="product_detail"),
    path("order_confirmation", views.order_confirmation, name="order_confirmation"),
    path("shopping_history", views.shopping_history, name="shopping_history"),
    path("checkout", views.checkout, name="checkout"),
    path("cart", views.cart, name="cart"),
]