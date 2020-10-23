from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, bike_type, condition, deals, brand

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    types = None
    new_used = None
    which_brand = None
    answer = None


    if request.GET:
        if 'bike_type' in request.GET:
            types = request.GET['bike_type'].split(',')
            products = products.filter(bike_type__name__in=types)
            types = bike_type.objects.filter(name__in=types)

        if 'condition' in request.GET:
            new_used = request.GET['condition'].split(',')
            products = products.filter(condition__name__in=new_used)
            new_used = condition.objects.filter(name__in=new_used)
        
        if 'brand' in request.GET:
            which_brand = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=which_brand)
            which_brand = brand.objects.filter(name__in=which_brand)

        if 'deals' in request.GET:
            answer = request.GET['deals'].split(',')
            products = products.filter(deals__name__in=answer)
            answer = deals.objects.filter(name__in=answer)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(seller_notes__icontains=query) | Q(SKU__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_type': types,
        'current_condition': new_used,
        'current_brand': which_brand,
        'current_deal': answer,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def bike_type_landing(request):

    return render(request, 'products/bike_type_landing.html')

def condition_landing(request):

    return render(request, 'products/condition_landing.html')

def brand_landing(request):

    return render(request, 'products/brand_landing.html')

def deals_landing(request):

    return render(request, 'products/deals_landing.html')