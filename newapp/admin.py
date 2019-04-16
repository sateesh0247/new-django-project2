from _future_ import unicode_literals
from django.contrib import admin
from .models import Square
class Squaredetail(admin.Modeladmin):
    list_display = ('number', 'sqr')
admin.site.register(square,Squaredetail)
