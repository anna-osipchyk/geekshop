from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="имя")
    description = models.TextField(verbose_name="описание", blank=True)
    is_active = models.BooleanField(verbose_name="категория активна", default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name="product", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name="имя")
    image = models.ImageField(blank=True, upload_to="products_images")
    short_desc = models.TextField(max_length=60, blank=True, verbose_name="краткое описание")
    description = models.TextField(blank=True, verbose_name="описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="количество на складе")

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Contact(models.Model):
    phone = models.CharField(max_length=50, verbose_name="номер телефона")
    email = models.EmailField(max_length=254, verbose_name="электронная почта")
    city = models.CharField(max_length=128, default="Москва", verbose_name="город")
    address = models.CharField(max_length=254, verbose_name="адресс")

    def __str__(self):
        return f"{self.pk} {self.email}"
