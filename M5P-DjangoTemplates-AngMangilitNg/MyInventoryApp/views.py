"""
Jobelle Ang, 240242
Sebastian Mangilit, 242880
Gide Ng, 243225
16 March 2026

We hereby attest to the truth of the following facts:
We have not discussed the Python code in my program with anyone 
other than our instructor or the teaching assistants assigned to this course.
We have not used Python code obtained from another student, 
or any other unauthorized source, whether modified or unmodified.
If any Python code or documentation used in my program was 
obtained from another source, it has been clearly noted with 
citations in the comments of our program.
"""

from django.shortcuts import render
from MyInventoryApp.models import Supplier, WaterBottle

def view_suppliers(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_suppliers.html', {'suppliers':supplier_objects})

def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles':bottle_objects})   

def add_bottles(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottles.html', {'suppliers': supplier_objects})    