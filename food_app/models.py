from django.db import models
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    name = models.CharField(max_length=128)
    short_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='food_images/')
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "fast food mahsuloti"
        verbose_name_plural = "faqat fast food mahsulotlari"

