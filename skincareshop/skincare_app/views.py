from django.shortcuts import render, redirect

from skincare_app.forms import ProductForm
from skincare_app.models import Product


# Create your views here.


def index(request):
    products = Product.objects.order_by('-release_date')[:3]
    return render(request, 'index.html', {'products': products})


def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.image = form.cleaned_data['image']
            product.save()
            return redirect('products')

    form = ProductForm()
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products, "form": form})


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form_data = ProductForm(request.POST, instance=product)
        if form_data.is_valid():
            form = form_data.save()
        return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit-product.html', {"form": form, "product": product})


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('products')
