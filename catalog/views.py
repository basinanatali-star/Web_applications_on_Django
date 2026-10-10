from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)
from .models import Product, Category, Blog
from .forms import ProductForm
from catalog.forms import ProductModeratorForm


class HomeView(TemplateView):
    def get(self, request):
        return render(request, "home.html")


class ContactsView(TemplateView):
    def get(self, request):
        return render(request, "contacts.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    pk_url_kwarg = "product_id"

    def get_success_url(self):
        return reverse_lazy(
            "catalog:product_detail",
            kwargs={
                "product_id": self.object.pk,
            },
        )
    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and ("catalog.can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
    pk_url_kwarg = "product_id"


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "product_id"

class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        product.is_published = False
        product.save(update_fields=['is_published'])

        return redirect('catalog:products_list')


class CategoryListView(ListView):
    model = Category
    template_name = "category_page.html"
    context_object_name = "categories"


class BlogCreateView(CreateView):
    model = Blog
    fields = [
        "title",
        "content",
        "preview",
        "publication_flag",
    ]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("catalog:blog_list")


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Blog.objects.filter(publication_flag=True).order_by("-creation_date")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "blog_id"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.number_of_views += 1
        obj.save(update_fields=["number_of_views"])

        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = [
        "title",
        "content",
        "preview",
        "publication_flag",
    ]
    pk_url_kwarg = "blog_id"

    def get_success_url(self):
        return reverse_lazy(
            "catalog:blog_detail",
            kwargs={
                "blog_id": self.object.pk,
            },
        )


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("catalog:blog_list")
    pk_url_kwarg = "blog_id"
