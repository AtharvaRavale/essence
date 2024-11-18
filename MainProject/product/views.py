from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Brand,Category
# Create your views here.
from .models import Product
from .models import ProductImages

from .models import Brand







from django.contrib.auth.models import User
from cart.models import *


def cart_items(request):
     u=get_object_or_404(User,username=request.user)
     product=Cart.objects.filter(user=u)
     data=[]
     for x in product:
          y=dict()
          y['image']=ProductImages.objects.filter(product=x.id).first()
          y['product']=x
          data.append(y)
     return data

def brandlist(request):
    
    data=Brand.objects.all()
    context = {
        'brands' : data
    }
    return render(request,'product/brandlist.html',context)


    




class AddProduct(View):
    def get(self,request):
        brands=Brand.objects.all()
        context={
            'brands':brands

        }
        return render(request,'product/create_product.html',context)
    
    def post(self,request):
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        brand=request.POST.get('brand')
        Product.objects.create(
            name=name,
            price_inclusive =price,
            description=description,

            features=''
        )
        

        return redirect('/')
    



def fetch_image_in_dictionary(image_obj,product_obj):
     result =dict()
     for image in image_obj:
          if(len(result)==2):
               break
          if image.product.id==product_obj.id:
               result[chr(65+len(result))]=image
     return result
          
     






def product_list(request):
        products_objects=Product.objects.all()
        images=ProductImages.objects.all()
        products=[]
        for product_obj in products_objects:
             image=fetch_image_in_dictionary(images,product_obj)
             products.append({
                  'details':product_obj,
                  'images': image
                   
             })
             
        categories = Category.objects.all()
        context ={
            'products':products,
            'categories':categories,
            'product':cart_items(request),
            
         }
        return render(request,'product/shop.html',context)


def product_details(request,id):
        product=get_object_or_404(Product,id=id)
        images=ProductImages.objects.filter(product=product)
        context={
            'product':product,
            'images':images


        }
        return render(request,'product/product_details.html',context)



#data=Brand.objects.all()
   # context = {
     #   'brands' : data
    #}
    #return render(request,'product/brandlist.html',context)








def update_product(request,id):
    product=get_object_or_404(Product,id=id)
    brands=Brand.objects.all()
    if request.method=='GET':
         context={
              'product':product,
              'brands' :brands
         }
         return render(request,'product/update_product.html',context)
    
    elif request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        brand=request.POST.get('brand')
        product.name=name
        product.price_inclusive=price
        product.description=description
        product.brand=Brand.objects.get(name=brand)
        product.save()
        return redirect('product_list')
    
from .forms import *
def add_brand(request):
     brand_form=BrandCreationform()
     context={
          'form':brand_form
     }
     return render(request,'product/add_entity.html',context)



def add_product_with_django_form(request):
     product_form = ProductCreationform()
     context={
          'form':product_form
     }
     return render(request,'product/add_entity.html',context)
     
      
         





