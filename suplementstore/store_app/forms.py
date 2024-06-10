from django import forms
from .models import Supplement


class SupplementForm(forms.ModelForm):
    class Meta:
        model = Supplement
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(SupplementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'available':
                visible.field.widget.attrs['class'] = 'form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-check-input'

