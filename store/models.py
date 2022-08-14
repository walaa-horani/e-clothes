from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.forms import FloatField, ModelForm
from datetime import datetime
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# Create your models here.



class Category(MPTTModel):
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField()


    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '/'.join(full_path[::-1])      


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    city =  models.CharField(max_length=50)
    country =  models.CharField(max_length=50)
   
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,null=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    latest = models.BooleanField(null=True,blank=True)
    


    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('new','new'),
        ('accepted','accepted'),
        ('canceled','canceled'),
    )
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False,null=True)
    first_name = models.CharField(max_length=100)
    last_name=  models.CharField(max_length=100)  
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    city =  models.CharField(max_length=50)
    country =  models.CharField(max_length=50)
    total = models.FloatField()
    status = models.CharField(max_length=10,choices=STATUS,default='new')
    ip = models.CharField(blank=True,max_length=20)
  
  
  
    def __str__(self):
        return self.customer.first_name  


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','address','phone','city','country']





class OrderProduct(models.Model):
    STATUS = (
        ('new','new'),
        ('accepted','accepted'),
        ('canceled','canceled'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added =   models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name

   

class ShippingAddress(models.Model) :
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    address = models.CharField(max_length=300,null=False)
    city = models.CharField(max_length=300,null=False)
    state = models.CharField(max_length=300,null=False)
    zipcode = models.CharField(max_length=300,null=False)
    


    def __str__(self):
        return self.address



class ShopCart(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.IntegerField()
    

    def __str__(self):
        return self.product.name


    @property
    def price(self):
        return(self.product.price)   

    @property
    def amout(self):
        return(self.quantity * self.product.price)      


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields= ['quantity']