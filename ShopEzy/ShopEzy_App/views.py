from django.shortcuts import render
# from models import customers
# Create your views here.

def index(request):
    return render(request, 'index.html')

def customer_signup(request):
    return render(request, 'customer_signup.html')

def customer_signin(request):
    return render(request, 'customer_signin.html')

def customer_profile(request):
    return render(request, 'customer_profile.html')

def product_view(request):
    return render(request, 'product_view.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def shopping_history(request):
    return render(request, 'shopping_history.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')
