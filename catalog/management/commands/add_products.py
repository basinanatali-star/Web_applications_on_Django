from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command


class Command(BaseCommand):
    help = "Добавление тестовых продуктов в базу"

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Мобильные приложения", description="развивающие игры для детей"
        )

        products = [
            {
                "name": "Смешарики. Учимся читать",
                "description": "Приложение, которое помогает пройти путь от первого знакомства с буквами до "
                               "уверенного составления слов и предложений. Вместе с любимыми героями: учим буквы, "
                               "читаем по слогам, расширяем словарный запас и проводим время с пользой!",
                "category": category,
                "price": "300",
                "created_at": "2022-01-30",
                "updated_at": "2022-01-30",
            },
            {
                "name": "Математика для детей. Фиксики",
                "description": "Подготовка к школе теперь тоже игра, причем учить счет, сложение, вычитание, часы, "
                               "дни недели и многое другое, ребенок сможет даже самостоятельно, вместе с "
                               "героями мультфильма. Фиксики расскажут и повторят, что нужно сделать.",
                "category": category,
                "price": "300",
                "created_at": "2018-10-31",
                "updated_at": "2018-10-31",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Продукт успешно добавлен: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"продукт уже существует: {product.name}")
                )

        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Данные успешно загружены из fixture"))
