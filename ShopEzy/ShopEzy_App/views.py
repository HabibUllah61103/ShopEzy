from django.shortcuts import render, redirect, get_object_or_404
from .models import Electronics, Garments, Groceries, Products, Shoppingcarts, Customers, Cartcontainers
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
        form = SigninForm(request.POST)
        if form.is_valid():
            cemail = form.cleaned_data['cemail']
            cpassword = form.cleaned_data['cpassword']
            user = authenticate(request, cemail=cemail, cpassword=cpassword)
            if user is not None:
                login(request, user)
                customer_id= request.user.custid
                return redirect('product_view', customer_id=customer_id)           
            else:
                return render(request, 'customer_signin.html', {'form': form})
    else:
        form = SigninForm()
    return render(request, 'customer_signin.html', {'form': form})

def customer_profile(request):
    return render(request, 'customer_profile.html')

def product_view(request, customer_id):
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
        'customer_id': customer_id,
    }
    return render(request, 'product_view.html', context)

def product_detail(request, category_name, customer_id):
    customer_id = int(customer_id)
    if request.method == 'POST':
        product_id = request.POST.get('prodid')
        customer_instance = get_object_or_404(Customers, custid=customer_id)
        product_instance = get_object_or_404(Products, prodid=int(product_id))
        shoppingcarts = Shoppingcarts.objects.all() 
        for shoppingcart in shoppingcarts:
            if int(customer_id) == shoppingcart.custid.custid:
                cartcontainers_instance = get_object_or_404(Cartcontainers, cartid=shoppingcart.cartid)
                print("old customer")
                if int(product_id) == cartcontainers_instance.prodid.prodid:
                    print('product already in cart')
                else:
                    shoppingcart_instance = get_object_or_404(Shoppingcarts, custid = customer_instance)
                    Cartcontainers.objects.create(prodid=product_instance, cartid=shoppingcart_instance)
                    print('cart container created')
            elif int(customer_id) != shoppingcart.custid.custid:
                print("new customer")
                Shoppingcarts.objects.create(custid=customer_instance)
                shoppingcart_instance = get_object_or_404(Shoppingcarts, custid = customer_instance)
                Cartcontainers.objects.create(prodid=product_instance, cartid=shoppingcart_instance)

        return redirect('product_detail', category_name=category_name, customer_id=customer_id)
    else:                
        if category_name == 'category_electronics':
            electronics = Electronics.objects.all()
            electronic_ids = [electronic.prodid.prodid for electronic in electronics]
            electronics_prod =[Products.objects.get(prodid=str(id)) for id in electronic_ids]
            for item in electronics_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
            context = {
            'products': electronics_prod,
            }
            return render(request, 'product_detail.html', context=context)
        
        elif category_name == 'category_garments':
            garments = Garments.objects.all()
            garment_ids = [garment.prodid.prodid for garment in garments]
            garments_prod =[Products.objects.get(prodid=str(id)) for id in garment_ids]
            for item in garments_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
            context = {
            'products': garments_prod,
            }
            return render(request, 'product_detail.html', context=context)
        
        else:
            groceries = Groceries.objects.all()
            grocery_ids = [grocery.prodid.prodid for grocery in groceries]
            groceries_prod =[Products.objects.get(prodid=str(id)) for id in grocery_ids]
            for item in groceries_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
            context = {
            'products': groceries_prod,
            }
            return render(request, 'product_detail.html', context=context)

def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def shopping_history(request):
    return render(request, 'shopping_history.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')
