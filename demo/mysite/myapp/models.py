from django.db import models

# Create your models here.
class stock_entry(models.Model):      
    
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    cost_price = models.IntegerField()
    aval_stock = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    
class product_list(models.Model):
           
    product_id = models.IntegerField(max_length=10)
    product_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    cost_price = models.IntegerField()

class customer(models.Model):
    c_name = models.CharField(max_length=50)
    c_contact = models.IntegerField(default=10)
    date = models.DateTimeField(auto_now=True)
    tot_items = models.IntegerField()
    tot_cost = models.IntegerField()
    adress = models.CharField(max_length=100)
    order = models.CharField(max_length=50)

class supplier(models.Model):
    s_name = models.CharField(max_length=50)
    s_agency = models.CharField(max_length=30)
    s_contact = models.IntegerField(default=10) 
    s_address = models.CharField(max_length=100)
