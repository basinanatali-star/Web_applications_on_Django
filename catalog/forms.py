from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


def clean_forbidden_words(text: str) -> str:
    """Проверяет текст на наличие запрещённых слов (в любом регистре)"""

    from django.core.exceptions import ValidationError

    if not text:
        return text

    text_lower = text.lower()
    found_words = [word for word in FORBIDDEN_WORDS if word in text_lower]

    if found_words:
        raise ValidationError(
            f"В тексте обнаружены запрещённые слова: {', '.join(found_words)}. "
            "Используйте другие формулировки."
        )

    return text


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
            "created_at",
            "updated_at",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Описание продукта"}
        )

        self.fields["category"].widget.attrs.update({"class": "form-control"})

        self.fields["price"].widget.attrs.update({"class": "form-control"})

        self.fields["created_at"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "date",
                "placeholder": "Формат: ДД.ММ.ГГГГ",
            }
        )

        self.fields["updated_at"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "date",
                "placeholder": "Формат: ДД.ММ.ГГГГ",
            }
        )

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        return clean_forbidden_words(name)

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        return clean_forbidden_words(description)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            return price

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")

        return price
