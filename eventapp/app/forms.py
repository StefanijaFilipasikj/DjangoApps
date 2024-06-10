from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['user', 'number_of_bands']

    def __init__(self, *args, **kwargs):
        bands = kwargs.pop('bands', [])
        super(EventForm, self).__init__(*args, **kwargs)
        self.initial['bands'] = ",".join(bands)
        for visible in self.visible_fields():
            if visible.name != 'open':
                visible.field.widget.attrs['class'] = 'form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-check-input'
