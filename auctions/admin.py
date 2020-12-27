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

admin.site.register(User, UserAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment)

