import uuid
from django.db import models

from django.core.validators import RegexValidator, MinValueValidator


class Company(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(verbose_name='Company name', max_length=100)
    company_location = models.CharField(verbose_name='Company location', max_length=100)


class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(verbose_name='First name', max_length=50)
    surname = models.CharField(verbose_name='Surname', max_length=50)
    company_name = models.ForeignKey(Company, verbose_name='Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class Manager(models.Model):
    class Meta:
        db_table = 'managers'
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    first_name = models.CharField(verbose_name='First name', max_length=50)
    surname = models.CharField(verbose_name='Surname', max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    departure_location = models.CharField(verbose_name='Departure location', max_length=100)
    delivery_location = models.CharField(verbose_name='Delivery location', max_length=100)
    container_type = models.CharField(verbose_name="Container's type", max_length=20)
    container_weight = models.IntegerField(verbose_name="Container's weight")
    # For future updates
    # Does it require foreign key?
    # cargo_type = models.CharField()
    # MoneyField?
    # price = models.IntegerField()
    #
    # client = models.ForeignKey()
    # manager = models.ForeignKey()

    def __str__(self):
        return f'{self.departure_location} {self.delivery_location}'
