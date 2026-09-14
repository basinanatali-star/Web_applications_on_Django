from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_view, contacts_view, products_list, product_detail, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products_list/', products_list, name='products_list'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('', home_view, name='home_view'),
    path('contacts/', contacts_view, name='contacts_view'),
]
