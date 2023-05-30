from django import forms
from django.forms import ModelForm, ValidationError
from .models import Kategoria, Edesseg

class EdessegForm(ModelForm):
    class Meta:
        model = Edesseg
        fields = '__all__'
        widgets = {
            'kategoria_azon': forms.Select(attrs = {'class': 'form-control'}),
            'nev': forms.TextInput(attrs = {'class': 'form-control'}),
            'leiras': forms.Textarea(attrs = {'class': 'form-control'}),
            'ar': forms.NumberInput(attrs = {'class': 'form-control'}),
            'kep_utvonal': forms.TextInput(attrs = {'class': 'form-control'})
        }

    def clean_ar(self):
        super().clean()
        ar = self.cleaned_data.get('ar', None)
        if(ar < 0):
            raise ValidationError('Az ár nem lehet negatív szám!')
        return ar