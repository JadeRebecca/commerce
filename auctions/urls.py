from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("categorie", views.categorie, name="categorie"),
    path("listing_categorie/<int:cat_id>", views.listing_categorie, name="listing_categorie"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist")
]
