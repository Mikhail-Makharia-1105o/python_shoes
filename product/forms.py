from .models import *
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'stock', 'manufacturer', 'supplier']

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'address']