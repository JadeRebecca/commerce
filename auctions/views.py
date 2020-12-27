from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Categorie


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

def listing(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, "auctions/listing.html",{
        "listing": listing
    })

def categorie(request):
    categories = Categorie.objects.all()
    return render(request, "auctions/categorie.html",{
        "categories" : categories
    })

#def listings_categorie(request, id):
    #return render(request, "auctions/create.html")
    # listing = Listing.objects.get(categorie=id)
    # return render(request, "auctions/index.html",{
    #     "listing": listing
    # })


def create(request):
    return render(request, "auctions/create.html")

def watchlist(request):
    #listings = User.watchlist.all()
    user = User.objects.get(username="jade")
    listing = user.watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "user" : user,
        "listing" : listing
    })
