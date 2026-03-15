from django.shortcuts import render
from MyInventoryApp.models import Supplier, WaterBottle

def view_base(request):
    return render(request, 'MyInventoryApp/base.html')

def view_suppliers(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_suppliers.html', {'suppliers':supplier_objects})

def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles':bottle_objects})   

def add_bottles(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottles.html', {'suppliers': supplier_objects})    