from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Categorie, Listing, Bid, Comment

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    filter_horizontal = ("watchlist",)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "start_at", "categorie", "active")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "amount", "user", "winner", "created_at")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "user", "comment", "created_at")

admin.site.register(User, UserAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)

