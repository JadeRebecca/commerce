from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title','description','start_at','starting_bid','categorie','picture']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
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