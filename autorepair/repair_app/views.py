from django.shortcuts import render, redirect

from repair_app.forms import RepairForm
from repair_app.models import Repair


# Create your views here.


def index(request):
    return render(request, "index.html")


def repairs(request):
    if request.method == 'POST':
        form = RepairForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.image = form.cleaned_data['image']
            repair.save()

    form = RepairForm()
    repairs = Repair.objects.filter(automobile__type='Sudan', user=request.user).values()
    return render(request, "repairs.html", {"repairs": repairs, "form": form})
