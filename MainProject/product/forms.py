from django.forms import ModelForm
from .models import Brand,Product


class BrandCreationform(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
    field_order=['name',
                 'logo',
                 'orgin',
                 'tagline',
                 'types',
                 'since',]
    


class ProductCreationform(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
