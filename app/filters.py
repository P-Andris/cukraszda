import django_filters
from django import forms
from .models import Kategoria, Edesseg

class EdessegFilter(django_filters.FilterSet):
    kategoria_azon = django_filters.ModelChoiceFilter(
        label = 'Kategória',
        field_name = 'kategoria_azon',
        queryset = Kategoria.objects.all(),
        widget = forms.Select(attrs = {'class': 'form-control'})
    )
    
    class Meta:
        model = Edesseg
        fields = ['kategoria_azon']