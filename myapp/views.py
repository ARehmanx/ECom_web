from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Products, Categories, Brands, PdctImgs, Reviews, Cart, Address, Order_Items, Complete_Order


# Create your views here.
def index(request):
    cart_products = Cart.objects.all()
    categories = Categories.objects.all()
    all_pdct = Products.objects.all()
    brands = Brands.objects.all()
    mob = Products.objects.filter(categories__category='Mobile')
    tab = Products.objects.filter(categories__category='Tablet')
    y = 0
    for pdcts in cart_products:
        y = y + 1
    context = {'pdct': all_pdct,
               'mob': mob,
               'categories': categories,
               'brands': brands,
               'tab': tab,
               'cart_products': cart_products,
               'y': y
               }
    return render(request, 'myapp/index.html', context)


def product(request, id):
    cart_products = Cart.objects.all()
    specific_brand = Products.objects.filter(brands__id=id)
    category_under_brand = Categories.objects.all()
    brand = Brands.objects.get(id=id)

    context = {
        'specific_brand': specific_brand,
        'category_under_brand': category_under_brand,
        'brand': brand,
        'cart_products': cart_products
    }
    return render(request, 'myapp/product.html', context)


def product_detail(request, item_id):
    cart_products = Cart.objects.all()
    specif_product_id = item_id
    all_pdct = Products.objects.all()
    details = Products.objects.get(id=item_id)
    product_img = PdctImgs.objects.filter(product_id=item_id)
    detailed_review = Reviews.objects.filter(product_id=item_id)
    r = 0
    for x in detailed_review:
        r = r + 1
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        title = request.POST.get('title')
        review = request.POST.get('review')
        rating = request.POST.get('ratingzz')
        Reviews(product_id=product_id, name=name, title=title, review=review, rating=rating).save()

    context = {'details': details,
               'all_pdct': all_pdct,
               'product_img': product_img,
               'specif_product_id': specif_product_id,
               'detailed_review': detailed_review,
               'r': r,
               'cart_products': cart_products,
               }

    return render(request, 'myapp/product_detail.html', context)


def add_to_cart(request, id):
    cart_pdct = Products.objects.get(id=id)
    try:
        pdct = Cart.objects.get(product_id=cart_pdct.id)
        pdct.quantity += 1
        pdct.total_price = pdct.quantity * cart_pdct.price
        pdct.save()
    except:
        cart = Cart.objects.create(product=cart_pdct)
        cart.total_price = cart.quantity * cart.product.price
        cart.save()
    return redirect('product_detail', id)


def checkout_cart(request):
    cart_products = Cart.objects.all()
    x = 0
    for prices_of_products in cart_products:
        x = x + prices_of_products.total_price
    y = 0
    for pdcts in cart_products:
        y = y + 1
    context = {'cart_products': cart_products, 'x': x, 'y': y}
    '''if request.method == 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        quantity = request.POST.get('product_quantity')
        total_price = request.POST.get('total_price')
        Cart(product_id=product_id, name=name, price=price, quantity=quantity, total_price=total_price).save()'''
    return render(request, 'myapp/checkout_cart.html', context)


def product_category_detail(request, id):
    pass


def checkout_info(request):
    cart_products = Cart.objects.all()
    checkout_cart = Cart.objects.all()
    context = {'checkout_cart': checkout_cart, 'cart_products': cart_products}
    return render(request, 'myapp/checkout_info.html', context)


def checkout_complete(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        phone_num = request.POST.get('phone_num')
        street_address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        Address(f_name=f_name, l_name=l_name, phone_num=phone_num, street_address=street_address,
                zip_code=zip_code).save()
    a = Cart.objects.all()
    a = a.delete()
    ordered_item = Order_Items.objects.all()
    context = {'ordered_item': ordered_item}
    return render(request, 'myapp/checkout_complete.html', context)


def add_to_order(request):
    cart_products = Cart.objects.all()
    for pdcts in cart_products:
        z = pdcts.product
        q = pdcts.quantity
        tp = pdcts.total_price
        c = Order_Items.objects.create(name=z, quantity=q, total_price=tp)
    return redirect('checkout_info')


def complete_payment(request):
    cart_products = Cart.objects.all()
    x = 0
    for prices_of_products in cart_products:
        x = x + prices_of_products.total_price
    context = {'cart_products': cart_products, 'x': x}
    return render(request, 'myapp/checkout_complete.html', context)


def delete_cart(request):
    Cart.objects.all().delete()
    return redirect('order_done')


def last_page(request):
    return render(request, 'myapp/checkout_complete.html')


def delete_order(request):
    order_item = Order_Items.objects.all()
    address = Address.objects.all()
    #a = Complete_Order.objects.create(order=order_item.name, address=address)
    #a.save()
    #Complete_Order.name = order_item
    #Complete_Order.address = address
    #Complete_Order.save()
    Order_Items.objects.all().delete()
    Address.objects.all().delete()
    return redirect('/')
