from django.shortcuts import render, redirect
from .models import Supplement
from .forms import SupplementForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def supplements(request):
    supplements = Supplement.objects.all()
    return render(request, 'supplements.html', {"supplements": supplements})


def supplement_details(request, supplement_id):
    supplement = Supplement.objects.get(id=supplement_id)
    return render(request, 'supplement_details.html', {"supplement": supplement})


def add_supplement(request):
    if request.method == 'POST':
        form_data = SupplementForm(request.POST, files=request.FILES)
        if form_data.is_valid():
            form = form_data.save(commit=False)
            form.user = request.user
            form.image = form_data.cleaned_data['image']
            form.save()
            return redirect('supplements')

    form = SupplementForm()
    return render(request, 'supplement_form.html', {"form": form})


def edit_supplement(request, supplement_id):
    supplement = Supplement.objects.get(id=supplement_id)
    if request.method == 'POST':
        form_data = SupplementForm(request.POST, instance=supplement, files=request.FILES)
        if form_data.is_valid():
            form = form_data.save(commit=False)
            form.user = request.user
            form.image = form_data.cleaned_data['image']
            form.save()
            return redirect('supplements')

    form = SupplementForm(instance=supplement)
    return render(request, 'supplement_form.html', {"form": form})


def delete_supplement(request, supplement_id):
    supplement = Supplement.objects.get(id=supplement_id)
    supplement.delete()
    return redirect('supplements')
