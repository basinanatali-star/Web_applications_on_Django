from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(max_length=150, verbose_name="Описание")

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(max_length=150, verbose_name="Описание")
    image = models.ImageField(upload_to="picture/", verbose_name="Изображение")
    category = models.CharField(max_length=150, verbose_name="Категория")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Цена за покупку"
    )
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]
