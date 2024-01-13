from django.urls import path
from ShopEzy_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
]