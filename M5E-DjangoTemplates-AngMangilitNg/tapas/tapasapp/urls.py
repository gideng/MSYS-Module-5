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

from django.urls import path
from . import views


urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
]