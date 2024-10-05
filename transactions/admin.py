from django.contrib import admin
from .models import (
    SaleBill, 
    SaleItem,
   
)


admin.site.register(SaleBill)
admin.site.register(SaleItem)
