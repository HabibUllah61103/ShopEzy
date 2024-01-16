from django.shortcuts import render
from .models import Electronics, Products, Garments, Groceries
# Create your views here.

def index(request):

    electronics = Electronics.objects.all()[:4]
    garments = Garments.objects.all()[:4]
    groceries = Groceries.objects.all()[:4]

    electronics_items_ids = [electronic.prodid.prodid for electronic in electronics]
    garments_items_ids = [garment.prodid.prodid for garment in garments]
    groceries_items_ids = [grocery.prodid.prodid for grocery in groceries]

    electronics_items = [Products.objects.get(prodid=id) for id in electronics_items_ids]
    garments_items = [Products.objects.get(prodid=id) for id in garments_items_ids]
    groceries_items = [Products.objects.get(prodid=id) for id in groceries_items_ids]

    for item in electronics_items:
        '''
        path = 'media/' + str(item.pspecs)
        with open(path, 'r') as file:
            file_contents = file.read()
        item.pspecs = file_contents
        '''
        item.pimage = item.pimage.decode('utf-8')
        

    for item in garments_items:
        '''
        path = 'media/' + str(item.pspecs)
        with open(path, 'r') as file:
            file_contents = file.read()
        item.pspecs = file_contents
        '''
        item.pimage = item.pimage.decode('utf-8')

    for item in groceries_items:
        '''
        path = 'media/' + str(item.pspecs)
        with open(path, 'r') as file:
            file_contents = file.read()
        item.pspecs = file_contents
        '''
        item.pimage = item.pimage.decode('utf-8')

    context={'electronics_items': electronics_items,
             'garments_items': garments_items,
             'groceries_items': groceries_items,
    }
    return render(request, 'index.html', context)


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
