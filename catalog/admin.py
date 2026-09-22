from django.contrib import admin
from .models import Category, Product, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "creation_date",
        "publication_flag",
        "number_of_views",
    )

    list_filter = ("publication_flag",)

    search_fields = (
        "title",
        "content",
    )
