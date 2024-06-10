from django.shortcuts import render, redirect

from .forms import BalloonFlightForm
from .models import BalloonFlight
# Create your views here.


def index(request):
    return render(request, 'index.html')


def flights(request):
    if request.method == 'POST':
        form = BalloonFlightForm(request.POST, files=request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.image = form.cleaned_data['image']
            flight.save()
            return redirect('flights')

    form = BalloonFlightForm()
    flights = BalloonFlight.objects.filter(user=request.user, from_airport='Skopje').values()
    return render(request, 'flights.html', {"flights": flights, "form": form})
