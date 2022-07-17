from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    descriptions = models.TextField('Описание')
    price = models.PositiveBigIntegerField('Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
