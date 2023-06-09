from django.db import models


# Create your models here.
class Category(models.Model):
    # new_pk = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    distutils = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'№{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('pk',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')
    short_desc = models.CharField(max_length=128, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


