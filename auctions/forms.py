from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, required = True)

class BidForm(forms.Form):
    amount = forms.DecimalField(max_digits=5, decimal_places=2)