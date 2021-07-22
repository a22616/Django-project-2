from django.db import models
from datetime import datetime

 

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=200)
    cat = models.CharField(max_length=200,default='')
    desc = models.CharField(max_length=400)
    Price = models.IntegerField(default=0)
    pub_date = models.DateField(default="")
    product_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    

    def __str__(self):
        return self.Product_name

    

