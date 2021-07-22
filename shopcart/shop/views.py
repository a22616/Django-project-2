from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    #products = Product.objects.all()
    #n = len(products)
    allProds = []
    catprods = Product.objects.values('cat' , 'Product_id')
    cates = {item['cat'] for item in catprods}
    for cats in cates:
        prod = Product.objects.filter(cat=cats)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        #parms = {'no_of_slide':nSlide,'range':range(1,nSlide),'product':products}
        #allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
        allProds.append([prod,range(1,nSlides),nSlides])
    parms={'allProds':allProds }
    #print(catprods)
    #print(cates)
    #print(cats)
    #print(prod)
    return render(request, 'shop/template/index.html',parms)

    #{% for products, range(1, len(products)), nSlides in allProds %}

def productview(request,myid):
    product = Product.objects.filter(Product_id=myid)
    print(product)
    return render(request,'shop/template/prodview.html',{'product':product[0]})
