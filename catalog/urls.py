from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ContactsView,
    ProductsListView,
    ProductDetailView,
    CategoryListView,
    BlogCreateView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CategoryListView.as_view(), name="index"),
    path("products_list/", ProductsListView.as_view(), name="products_list"),
    path(
        "product_detail/<int:product_id>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("category_page/", CategoryListView.as_view(), name="category_page"),
    path("home_view/", HomeView.as_view(), name="home_view"),
    path("contacts/", ContactsView.as_view(), name="contacts_view"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:blog_id>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<int:blog_id>/edit/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:blog_id>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
