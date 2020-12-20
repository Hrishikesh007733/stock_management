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
   #return HttpResponse("hello number%s"% product_id)

def customer_cus(request):
    return render(request,'myapp/cushomepage.html')

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
    if request.method == "POST":
        c_name = request.POST.get('c_name',)
        c_contact = request.POST.get('c_contact',)
        tot_items = request.POST.get('tot_items',)
        tot_cost = request.POST.get('tot_cost',)
        adress = request.POST.get('adress',)
        order = request.POST.get('order',)
        date = request.POST.get('date',)
        
        placeorder = customer(c_name=c_name,c_contact=c_contact,tot_items=tot_items,tot_cost=tot_cost,adress=adress,order=order,date=date)
        placeorder.save()        
    return render(request,'myapp/orderplace.html')   

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

def index(request):
    stock_list = stock_entry.objects.all()
    #return render(request,'myapp/index.html')
    #return HttpResponse(stock_list)
    context={
        'stock_list':stock_list
    }
    return render(request,'myapp/index.html',context)