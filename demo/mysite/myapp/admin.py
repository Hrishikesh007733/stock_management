from django.contrib import admin
from .models import stock_entry
from .models import product_list
from .models import customer
from .models import supplier
# Register your models here.
admin.site.register(stock_entry)
admin.site.register(product_list)
admin.site.register(customer)
admin.site.register(supplier)