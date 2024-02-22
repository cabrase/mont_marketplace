from django import forms
from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'photo', 'price', 'condition', 'seller')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: Brand, model, '
                                                                                    'color, and size'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell others about your item'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'seller': forms.Select(attrs={'class': 'form-control'}),
        }
