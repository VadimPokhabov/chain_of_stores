from django.db import models

from trading.models import Factory, Network, Businessman


class BaseProduct(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=150, verbose_name='Модель')
    product_launch_date = models.DateTimeField(verbose_name='Дата выхода на рынок')

    class Meta:
        abstract = True


class FactoryProduct(BaseProduct):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.product_name}'

    class Meta:
        verbose_name = 'Продукт завода'
        verbose_name_plural = 'Продукты завода'


class NetworkProduct(BaseProduct):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.product_name}'

    class Meta:
        verbose_name = 'Продукт розничной сети'
        verbose_name_plural = 'Продукты розничных сетей'


class BusinessmanProduct(BaseProduct):
    entrepreneur = models.ForeignKey(Businessman, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.product_name}'

    class Meta:
        verbose_name = 'Продукт индивидуального предпринимателя'
        verbose_name_plural = 'Продукты индивидуальных предпринимателей'
