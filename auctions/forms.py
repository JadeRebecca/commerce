from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateTimeInput
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title','description','start_at','starting_bid','categorie','picture']
        labels = {
            'title': 'Title ',
            'description': 'Description ',
            'start_at': 'Start at ',
            'starting_bid': 'Starting bid ',
            'categorie': 'Categorie ',
            'picture': 'Picture '
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows':2, 'cols': 40})
        }
        
class CommentForm(forms.Form):
    comment = forms.CharField(
            widget=Textarea(attrs={'class': 'form-control'}), 
            required = True)

class BidForm(forms.Form):
    amount = forms.DecimalField(
            widget=NumberInput(attrs={'class': 'input-number'}), 
            max_digits=5, 
            decimal_places=2)