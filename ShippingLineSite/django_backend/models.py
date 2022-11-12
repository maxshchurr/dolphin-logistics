from django.db import models

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from djmoney.models.fields import MoneyField


class Company(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(verbose_name='Company name', max_length=100, unique=True, null=False)
    company_location = models.CharField(verbose_name='Company location', max_length=100, null=False)
    company_email = models.EmailField(verbose_name="Company's email", max_length=50, unique=True, null=False)

    # objects = models.Manager()


class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(verbose_name='First name', max_length=50)
    surname = models.CharField(verbose_name='Surname', max_length=50)
    company_name = models.ForeignKey(Company, verbose_name='Company', on_delete=models.CASCADE)
    client_email = models.EmailField(verbose_name="Client's email", max_length=50, unique=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class SalesManager(models.Model):
    class Meta:
        db_table = 'sales_managers'
        verbose_name = 'Sales Manager'
        verbose_name_plural = 'Sales Managers'

    first_name = models.CharField(verbose_name='First name', max_length=50)
    surname = models.CharField(verbose_name='Surname', max_length=50)
    sales_manager_email = models.EmailField(verbose_name="Manager's email", max_length=50, unique=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    types_of_containers = (
        ("20'DV (dry van)", "20'DV (dry van)"),
        ("20'OT (open top", "20'OP (open top)"),
        ("20'FR (flat rack)", "20'FR (flat rack)"),
        ("20'REF (refrigerated)", "20'REF (refrigerated)"),
        ("40'DV (dry van)", "40'DV (dry van)"),
        ("40'HC (high cube)", "40'HC (high cube)"),
        ("40'OT (open top)", "40'OP (open top)"),
        ("40'FR (flat rack)", "40'FR (flat rack)"),
        ("40'REF (refrigerated)", "40'REF (refrigerated)")
    )

    types_of_cargo = (
        ("FAK (freight all kinds)", "FAK (freight all kinds)"),
        ("IMO (dangerous cargo)", "IMO (dangerous cargo)")
    )

    departure_location = models.CharField(verbose_name='Departure location', max_length=100)
    delivery_location = models.CharField(verbose_name='Delivery location', max_length=100)
    container_type = models.CharField(verbose_name="Container's type", choices=types_of_containers, max_length=100)
    cargo_net_weight = models.IntegerField(verbose_name="Cargo's weight",
                                           validators=[MinValueValidator(1), MaxValueValidator(28000)])
    cargo_type = models.CharField(verbose_name='Type of cargo', choices=types_of_cargo, max_length=100)
    cargo = models.CharField(verbose_name='Cargo description', max_length=100)
    quantity_of_containers = models.IntegerField(verbose_name='Quantity of containers', validators=[MinValueValidator(1)])
    expected_date_of_freight = models.DateField(verbose_name='Expected date of freight')
    client = models.ForeignKey(Client, verbose_name='Client', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.departure_location} {self.delivery_location}'


class Quotation(models.Model):
    class Meta:
        db_table = "quotations"
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'

        freight_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=1)
        congestion_at_load_price = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=1)
        new_bunker_factor_price = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=1)
        term_handling_origin_price = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=1)
        # Must be added automatically with a date binding(approximately + 1 month to order's expected date of freight)
        # validity_date = models.DateField()

        manager = models.ForeignKey(SalesManager, verbose_name='Sales Manager', on_delete=models.RESTRICT)

        def __str__(self):
            return f'{self.manager}'
