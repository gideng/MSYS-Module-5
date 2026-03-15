from django.shortcuts import render
from MyInventoryApp.models import Supplier, WaterBottle

def view_supplier(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/suppliers.html', {'suppliers':supplier_objects})

def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottles.html', {'bottles':bottle_objects})   

def add_bottle(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': supplier_objects})    