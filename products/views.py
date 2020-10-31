from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, bike_type, condition, deals, brand, ProductReview
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    types = None
    new_used = None
    which_brand = None
    answer = None
    sort = None
    direction = None

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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                seller_notes__icontains=query) | Q(SKU__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

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
    reviews = ProductReview.objects.filter(product=product).order_by("-comment")

    context = {
        'product': product,
        'reviews': reviews,
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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def add_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        review = ProductReview()
        if request.method == 'POST':
            review.comment = request.POST["comment"]
            review.user = request.user
            review.product = product
            review.save()
            return redirect(reverse('product_detail', args=[product_id]))
    else:
        messages.error(request, "Sign up to leave a review.")
        return redirect("account_login")
