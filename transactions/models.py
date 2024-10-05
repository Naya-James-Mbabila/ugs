from django.db import models
from inventory.models import Stock
from decimal import Decimal

class SaleBill(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('Cash', 'Cash'),
        ('Momo', 'Momo'),
    ]

    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    mode_of_payment = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES, default='Cash')
    sales_agent = models.CharField(max_length=50)

    def __str__(self):
        return f"Bill no: {self.billno}"

    def get_items_list(self):
        return self.salebillno.all()
        
    def get_total_price(self):
        return sum(Decimal(item.totalprice) for item in self.salebillno.all())

class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Bill no: {self.billno.billno}, Item = {self.stock.name}"

    def save(self, *args, **kwargs):
        self.totalprice = Decimal(self.quantity) * Decimal(self.perprice)
        super().save(*args, **kwargs)

class SaleBillDetails(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='saledetailsbillno')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Bill no: {self.billno.billno}"

    def save(self, *args, **kwargs):
        self.total = self.billno.get_total_price()
        super().save(*args, **kwargs)