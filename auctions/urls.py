from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/<int:listing_id>/<str:username>", views.listing_logged_in, name="listing"),
    path("categorie", views.categorie, name="categorie"),
    path("listing_categorie/<int:cat_id>", views.listing_categorie, name="listing_categorie"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watchlist/<int:listing_id>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<int:listing_id>", views.remove_watchlist, name="remove_watchlist"),
    path("add_comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing")
    # path("add_bid/<int:listing_id>", views.add_bid, name="add_bid")
]
