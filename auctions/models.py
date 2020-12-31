from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class Categorie(models.Model):
    description = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.description}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    start_at = models.DateTimeField()
    starting_bid = models.DecimalField(max_digits=5, decimal_places=2,  blank=False, default='0.1')
    categorie = models.ForeignKey(Categorie, models.SET_NULL, blank=True, null=True )
    picture = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, related_name='watchers', blank=True)

class Bid(models.Model):
    listing  = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2,  blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    winner = models.BooleanField()

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False)

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title','description','start_at','starting_bid','categorie','picture']