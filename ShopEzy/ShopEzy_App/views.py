from django.shortcuts import redirect, render
from .models import Electronics, Garments, Groceries, Products
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
