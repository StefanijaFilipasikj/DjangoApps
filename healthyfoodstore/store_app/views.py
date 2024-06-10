from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def out_of_stock(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = form.cleaned_data['image']
            product.user = request.user
            product.save()
            return redirect('out_of_stock')

    form = ProductForm()
    out_of_stock = Product.objects.filter(quantity=0, category__active=True).values()
    return render(request, 'out_of_stock.html', {'out_of_stock': out_of_stock, "form": form})
