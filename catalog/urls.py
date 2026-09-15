from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_view, contacts_view, products_list, product_detail, category_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', category_page, name='index'),
    path('products_list/', products_list, name='products_list'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('category_page/', category_page, name='category_page'),
    path('home_view/', home_view, name='home_view'),
    path('contacts/', contacts_view, name='contacts_view'),
]
