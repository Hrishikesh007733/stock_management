from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('homepage/', views.manager_page),
    path('add_stock/', views.stock_add),
    path('productlist/',views.product_list),
    path('cushomepage/',views.customer_cus),
    path('orderplace/', views.place_order),
    path('supplierorder/', views.supplier_order),
]