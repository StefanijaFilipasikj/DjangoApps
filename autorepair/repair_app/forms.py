from django import forms
from repair_app.models import Repair


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
