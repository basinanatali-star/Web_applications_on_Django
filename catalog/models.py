from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(max_length=255, verbose_name="Описание")

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(max_length=255, verbose_name="Описание")
    image = models.ImageField(upload_to="picture/", verbose_name="Изображение")
    category = models.CharField(max_length=150, verbose_name="Категория")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Цена за покупку (₽)",
    )
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="picture/",
        verbose_name="Превью",
        blank=True,
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    publication_flag = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )
    number_of_views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ["publication_flag"]

    def __str__(self):
        return self.title
