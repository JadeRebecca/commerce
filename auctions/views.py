from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from .models import User, Listing, Categorie, ListingForm


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html",{
        "listings" : listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required
def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request, listing_id):
    listing_id = int(listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "auctions/listing.html",{
        "listing": listing
    })

def listing_categorie(request, cat_id):
    cat_id = int(cat_id)
    listings = Listing.objects.filter(categorie=cat_id)
    categorie = Categorie.objects.get(pk=cat_id)
    return render(request, "auctions/index.html",{
        "listings": listings,
        "categorie": categorie
    })

def categorie(request):
    categories = Categorie.objects.all()
    return render(request, "auctions/categorie.html",{
        "categories" : categories
    })

@login_required
def create(request):
    categories = Categorie.objects.all()
    if request.method == "POST":
        f = ListingForm(request.POST)
        if f.is_valid():
            new_listing = f.save()
            print("listing saved")
            return HttpResponseRedirect(reverse("listing", args=(new_listing.id,)))
        else:
            print("not saved")
            print(f.errors.as_data())
    return render(request, "auctions/create.html",{
        "categories": categories
    })
    
@login_required
def watchlist(request):
    listings = request.user.watchlist.all()
    return render(request, "auctions/index.html",{
        "listings" : listings,
        "watchlist": True
    })

@login_required
def add_watchlist(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=int(listing_id))
        request.user.watchlist.add(listing)
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))
