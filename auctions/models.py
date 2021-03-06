from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

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
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    watcher = models.ManyToManyField(User, related_name='watchlist', blank=True)

    def __str__(self):
        return f"{self.title}"
  

class Bid(models.Model):
    listing  = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2,  blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    winner = models.BooleanField(default=False)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False)