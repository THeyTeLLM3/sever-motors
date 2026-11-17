from django.core.validators import MinValueValidator
from django.db import models


class VehicleCategory(models.Model):
    name = models.CharField('Название категории', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория автомобилей'
        verbose_name_plural = 'Категории автомобилей'
        ordering = ['name']


class Workshop(models.Model):
    name = models.CharField('Название цеха', max_length=120, unique=True)
    building = models.CharField('Корпус', max_length=50)
    description = models.TextField('Назначение', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'
        ordering = ['name']


class Supplier(models.Model):
    name = models.CharField('Наименование', max_length=150, unique=True)
    email = models.EmailField('Электронная почта')
    phone = models.CharField('Телефон', max_length=30)
    city = models.CharField('Город', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']


class Vehicle(models.Model):
    name = models.CharField('Название модели', max_length=120, unique=True)
    category = models.ForeignKey(VehicleCategory, on_delete=models.PROTECT, verbose_name='Категория', related_name='vehicles')
    description = models.TextField('Описание')
    price = models.DecimalField('Цена, руб.', max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    power = models.PositiveIntegerField('Мощность, л. с.', validators=[MinValueValidator(1)])
    photo = models.ImageField('Фотография', upload_to='vehicles/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField('Выпускается', default=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'
        ordering = ['name']


class Part(models.Model):
    name = models.CharField('Название детали', max_length=150)
    article = models.CharField('Артикул', max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик', related_name='parts')
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена, руб.', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField('Остаток, шт.', default=0)
    photo = models.ImageField('Фотография', upload_to='parts/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.article} — {self.name}'

    class Meta:
        verbose_name = 'Комплектующая'
        verbose_name_plural = 'Комплектующие'
        ordering = ['name']


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=150)
    position = models.CharField('Должность', max_length=100)
    workshop = models.ForeignKey(Workshop, on_delete=models.PROTECT, verbose_name='Цех', related_name='employees')
    hired_on = models.DateField('Дата приёма')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['full_name']


class ProductionOrder(models.Model):
    number = models.CharField('Номер заказа', max_length=40, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, verbose_name='Модель', related_name='orders')
    workshop = models.ForeignKey(Workshop, on_delete=models.PROTECT, verbose_name='Цех', related_name='orders')
    quantity = models.PositiveIntegerField('Количество, шт.', validators=[MinValueValidator(1)])
    planned_on = models.DateField('Плановая дата')
    status = models.CharField('Статус', max_length=20, choices=[('planned', 'Запланирован'), ('in_progress', 'В работе'), ('completed', 'Завершён')], default='planned')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Производственный заказ'
        verbose_name_plural = 'Производственные заказы'
        ordering = ['-planned_on', '-pk']


class QualityCheck(models.Model):
    order = models.ForeignKey(ProductionOrder, on_delete=models.PROTECT, verbose_name='Заказ', related_name='quality_checks')
    inspector = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='Инспектор', related_name='quality_checks')
    checked_on = models.DateField('Дата проверки')
    passed = models.BooleanField('Проверка пройдена', default=False)
    notes = models.TextField('Результаты проверки')

    def __str__(self):
        return f'{self.order} — {self.checked_on:%d.%m.%Y}'

    class Meta:
        verbose_name = 'Проверка качества'
        verbose_name_plural = 'Проверки качества'
        ordering = ['-checked_on', '-pk']
