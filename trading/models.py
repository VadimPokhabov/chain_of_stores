from django.db import models


class BaseRetail(models.Model):
    """
    Базовая розничная торговля
    """
    name = models.CharField(max_length=350, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="email")
    country = models.CharField(max_length=150, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")
    arrears = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0, verbose_name="Задолженность")
    create_time = models.DateTimeField(verbose_name="Дата создания",
                                       auto_now_add=True)

    class Meta:
        abstract = True


class Factory(BaseRetail):
    """
    Модель завода
    """

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class Network(BaseRetail):
    """
    Модель розничной сети
    """

    supplier = models.ForeignKey(
        Factory, on_delete=models.CASCADE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class Businessman(BaseRetail):
    """
     Модель Индивидуального предпринимателя
    """

    supplier = models.ForeignKey(
        Network, on_delete=models.CASCADE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
