from django.shortcuts import render, redirect
from .models import Electronics, Garments, Groceries, Products
from django.contrib.auth import authenticate, login
from .forms import SigninForm, SignupForm
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

    for item in electronics_prod:
        item.pimage = item.pimage.decode('utf-8')
    for item in garments_prod:
        item.pimage = item.pimage.decode('utf-8')
    for item in groceries_prod:
        item.pimage = item.pimage.decode('utf-8')


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
            cpassword = form.cleaned_data['cpassword']
            cre_password = form.cleaned_data['cre_password']
            print(cpassword)
            print(cre_password)
            
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
        form = SigninForm(request.POST)
        if form.is_valid():
            cemail = form.cleaned_data['cemail']
            cpassword = form.cleaned_data['cpassword']
            user = authenticate(request, cemail=cemail, cpassword=cpassword)
            if user is not None:
                login(request, user)
                return redirect('product_view')           
            else:
                return render(request, 'customer_signin.html', {'form': form})
    else:
        form = SigninForm()
    return render(request, 'customer_signin.html', {'form': form})

def customer_profile(request):
    return render(request, 'customer_profile.html')

def product_view(request):
    electronics = Electronics.objects.all()
    garments = Garments.objects.all()
    groceries = Groceries.objects.all()
    products = Products.objects.all()
    eletronic_prod_id = {}
    garment_prod_id = {}
    grocery_prod_id = {}
        
    electronic_ids = [electronic.prodid.prodid for electronic in electronics]
    garment_ids = [garment.prodid.prodid for garment in garments]
    grocery_ids = [grocery.prodid.prodid for grocery in groceries]

    product_id_rating = [(product.prodid, product.rating) for product in products]
    for product_id, prodcut_rating in product_id_rating:
        if product_id in electronic_ids:
            eletronic_prod_id[product_id] = float(prodcut_rating)
        elif product_id in garment_ids:
            garment_prod_id[product_id] = float(prodcut_rating)
        elif product_id in grocery_ids:
            grocery_prod_id[product_id] = float(prodcut_rating)

    sorted_electronic_prod_id = dict(sorted(eletronic_prod_id.items(), key=lambda item: item[1], reverse=True))
    sorted_garment_prod_id = dict(sorted(garment_prod_id.items(), key=lambda item: item[1], reverse=True))
    sorted_grocery_prod_id = dict(sorted(grocery_prod_id.items(), key=lambda item: item[1], reverse=True))

    electronics_prod = [Products.objects.get(prodid=str(id)) for id in sorted_electronic_prod_id.keys()]
    garments_prod = [Products.objects.get(prodid=str(id)) for id in sorted_garment_prod_id.keys()]
    groceries_prod = [Products.objects.get(prodid=str(id)) for id in sorted_grocery_prod_id.keys()]


    context = {
        'electronics': electronics_prod,
        'garments': garments_prod,
        'groceries': groceries_prod,
    }
    return render(request, 'product_view.html', context)

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
