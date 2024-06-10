from django import forms

from balloon_app.models import BalloonFlight


class BalloonFlightForm(forms.ModelForm):
    class Meta:
        model = BalloonFlight
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(BalloonFlightForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
