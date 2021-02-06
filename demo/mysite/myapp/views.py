from django.shortcuts import render
from django.http import HttpResponse
from .models import stock_entry
from .models import customer
from .models import supplier

# Create your views here.
def welcome(request):
    return render(request, 'myapp/welcome.html')
    
def manager_page(request):
    return render(request,'myapp/homepage.html')

def details(request,product_id):
   stock = stock_entry.objects.get(id=product_id)   
   return render(request,'myapp/details.html',{'stock':stock}) 
   

def customer_cus(request):
    display= customer.objects.all()
    context={
        'display': display
    }
    return render(request,'myapp/cushomepage.html',context)

def stock_add(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id',)
        product_name = request.POST.get('product_name',)
        customer_name = request.POST.get('customer_name',)
        cost_price = request.POST.get('cost_price',)
        aval_stock = request.POST.get('aval_stock',)
        location = request.POST.get('location',)
        
        stock = stock_entry(product_id=product_id,product_name=product_name,customer_name=customer_name,cost_price=cost_price,aval_stock=aval_stock,location=location)
        stock.save()        
    return render(request,'myapp/add_stock.html')   

def place_order(request):
    place_order = stock_entry.objects.all()
    context={
        'place_order': place_order
    }
    if request.method == "POST":
        c_name = request.POST.get('c_name',)
        c_contact = request.POST.get('c_contact',)
        tot_items = request.POST.get('tot_items',)
        adress = request.POST.get('adress',)
        order = request.POST.get('order',)
        date = request.POST.get('date',)
        
        placeorder = customer(c_name=c_name,c_contact=c_contact,tot_items=tot_items,adress=adress,order=order,date=date)
        placeorder.save()

        item_id = int(order)
        no_of_items = int(tot_items)
        t = stock_entry.objects.get(id = item_id)
        t.aval_stock = t.aval_stock - no_of_items
        t.save()

    return render(request,'myapp/orderplace.html',context)      

def product_list(request):
    product_list = stock_entry.objects.all()
    context={
        'product_list': product_list
    }
    return render(request,'myapp/productlist.html',context)

def supplier_order(request):
    supplier_order = supplier.objects.all()
    context = {
        'supplier_order': supplier_order
    }
    return render(request,'myapp/supplierorder.html',context)  

