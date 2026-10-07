from django.core.mail import send_mail
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Product
from catalog.forms import ProductForm
from users.forms import UserRegisterForm
from users.models import CustomUser


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:category_page')

class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = "users/users_form.html"
    success_url = reverse_lazy("users:login")


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
        )
