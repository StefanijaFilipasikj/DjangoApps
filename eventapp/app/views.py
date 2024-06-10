from django.shortcuts import render, redirect

from .forms import EventForm
from .models import Event, Band, BandInEvent

# Create your views here.


def index(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form_data = EventForm(request.POST, files=request.FILES)
        if form_data.is_valid():
            event = form_data.save(commit=False)
            event.user = request.user
            event.poster = form_data.cleaned_data['poster']
            event.save()
            bands_names = form_data.cleaned_data['bands'].split(',')
            for band_name in bands_names:
                band = Band.objects.get(name=band_name)
                if band:
                    band.save()
                    BandInEvent.objects.create(band=band, event=event)
            return redirect('index')

    form = EventForm()
    return render(request, 'event_form.html', {"form": form})


def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form_data = EventForm(request.POST, files=request.FILES, instance=event)
        if form_data.is_valid():
            form = form_data.save(commit=False)
            form.user = request.user
            event.poster = form_data.cleaned_data['poster']
            event.save()
            bands_names = form_data.cleaned_data['bands'].split(',')
            bands_in_event = BandInEvent.objects.filter(event=event)
            for band_name in bands_names:
                band = Band.objects.filter(name=band_name).first()
                if band and not bands_in_event.filter(band=band).exists():
                    BandInEvent.objects.create(band=band, event=event)
            for band_in_event in bands_in_event:
                if not bands_names.__contains__(band_in_event.band.name):
                    band_in_event.delete()
            return redirect('index')

    bands_in_event = BandInEvent.objects.filter(event=event_id)
    bands = [b.band.name for b in bands_in_event]
    form = EventForm(instance=event, bands=bands)
    return render(request, 'event_form.html', {"form": form})


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('index')
