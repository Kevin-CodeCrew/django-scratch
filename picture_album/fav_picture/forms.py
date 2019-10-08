from django import forms
from .models import FavPictureModel


class FavEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fp_caption'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = FavPictureModel
        fields = ['fp_caption']

