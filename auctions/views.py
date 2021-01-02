from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max


from .models import User, Listing, Categorie, Bid, Comment
from .forms import CommentForm, BidForm, ListingForm


def index(request):
    listings = Listing.objects.all()
    for l in listings:
        if Bid.objects.filter(listing=l.id).exists():
            foundMax = Bid.objects.filter(listing=l.id).aggregate(Max('amount'))
            bidMax = foundMax['amount__max']
            l.bidMax = bidMax
        else:
            l.bidMax = l.starting_bid        
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

@login_required
def listing_logged_in(request, listing_id, username):
    listing_id = int(listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = Comment.objects.filter(listing=listing_id)
    #watchlist management
    if request.user.watchlist.filter(pk=listing.id).exists():
        in_my_watchlist = True
    else:
        in_my_watchlist = False
    context = {
        'listing' : listing,
        'comments' : comments,
        'in_my_watchlist' : in_my_watchlist
    }

    #bid management
    if Bid.objects.filter(listing=listing_id).exists():
        foundMax = Bid.objects.filter(listing=listing_id).aggregate(Max('amount'))
        bidMax = foundMax['amount__max']
        print("il y a une enchère max")
    else:
        bidMax = listing.starting_bid
        print("no bid yet")

    if request.method == "POST":
        form = BidForm(request.POST)
        custom_error = False
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount > bidMax :
                new_bid = Bid(listing= Listing.objects.get(pk=listing_id), user=request.user, amount=amount)
                new_bid.save()
                bidMax = amount
            else:
                custom_error = "You must place a bid superior to the current price!"
                print("custom error")
                context['custom_error'] = custom_error
        else:
            context['errors'] = form.errors.items()
              
    context['bidMax'] = bidMax
        
    bidForm = BidForm()
    form = CommentForm()
    context['bidForm'] = bidForm
    context['form'] = form

    return render(request, "auctions/listing.html", context) 

def listing(request, listing_id):
    listing_id = int(listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = Comment.objects.filter(listing=listing_id)
    return render(request, "auctions/listing.html",{
        "listing": listing,
        "comments": comments
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
            return HttpResponseRedirect(reverse("listing", args=(new_listing.id,)))
        else:
            print(f.errors.as_data())
    return render(request, "auctions/create.html",{
        "categories": categories
    })
    
@login_required
def watchlist(request):
    listings = request.user.watchlist.all()
    for l in listings:
        if Bid.objects.filter(listing=l.id).exists():
            foundMax = Bid.objects.filter(listing=l.id).aggregate(Max('amount'))
            bidMax = foundMax['amount__max']
            l.bidMax = bidMax
        else:
            l.bidMax = l.starting_bid        
    return render(request, "auctions/index.html",{
        "listings" : listings,
        "watchlist": True
    })

@login_required
def add_watchlist(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=int(listing_id))
        request.user.watchlist.add(listing)
        return HttpResponseRedirect(reverse("listing", args=(listing.id, request.user.username,)))

@login_required
def remove_watchlist(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=int(listing_id))
        request.user.watchlist.remove(listing)
        return HttpResponseRedirect(reverse("listing", args=(listing.id, request.user.username,)))

@login_required
def add_comment(request, listing_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            new_comment = Comment(listing= Listing.objects.get(pk=listing_id), user=request.user, comment=comment)
            new_comment.save()
            return HttpResponseRedirect(reverse("listing", args=(listing_id, request.user.username,)))

# @login_required
# def add_bid(request, listing_id):
#     if request.method == "POST":
#         form = BidForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data['amount']
#             new_bid = Bid(listing= Listing.objects.get(pk=listing_id), user=request.user, amount=amount)
#             new_bid.save()
#         else:
#             print(form.errors.items())
#         return HttpResponseRedirect(reverse("listing", args=(listing_id, request.user.username,)))
