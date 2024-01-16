from django.shortcuts import render, redirect
from .models import Electronics, Garments, Groceries, Products
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import SignupForm
# Create your views here.

def index(request):
    electronics = Electronics.objects.all()
    garments = Garments.objects.all()
    groceries = Groceries.objects.all()

    electronic_ids = [electronic.prodid.prodid for electronic in electronics]
    garment_ids = [garment.prodid.prodid for garment in garments]
    grocery_ids = [grocery.prodid.prodid for grocery in groceries]

    electronics_prod =[Products.objects.get(prodid=str(id)) for id in electronic_ids]
    garments_prod =[Products.objects.get(prodid=str(id)) for id in garment_ids]
    groceries_prod =[Products.objects.get(prodid=str(id)) for id in grocery_ids]

    # for item in electronics_prod:
    #     item.pimage = item.pimage.decode('utf-8')
    # for item in garments_prod:
    #     item.pimage = item.pimage.decode('utf-8')
    # for item in groceries_prod:
    #     item.pimage = item.pimage.decode('utf-8')


    context = {
        'electronics': electronics_prod,
        'garments': garments_prod,
        'groceries': groceries_prod,
    }
    return render(request, 'index.html', context)

def customer_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_signin')
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'customer_signup.html', context=context)

def customer_signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cemail = form.cleaned_data['cemail']
            cpassword = form.cleaned_data['cpassword']
            user = authenticate(request, cemail=cemail, cpassword=cpassword)
            if user is not None:
                login(request, user)
                print(request.user.custid)
                return redirect('product_view')           
            else:
                return render(request, 'customer_signin.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'customer_signin.html', {'form': form})

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
