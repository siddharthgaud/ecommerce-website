from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Products(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default='',blank=True, null=True)
    image = models.ImageField(upload_to='upolads/products/') 

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category_id=category_id)
        else:
            return Products.get_all_products()
        
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)    



class Customer(models.Model):
    first_name=models.CharField(max_length=50)   
    last_name=models.CharField(max_length=50)   
    phone=models.CharField(max_length=10)  
    email=models.EmailField(default='')
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)#field
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):#1
        return Order.objects.filter(customer=customer_id).order_by('-date')
    


class slider(models.Model):
    title = models.CharField(max_length=100,blank=False,default="")
    description = models.TextField(max_length=100,blank=False,default="")
    image1 = models.ImageField(upload_to='uploads/slider/',blank=False)   

    def __str__(self):
        return self.title

    def get_all_sliders():
        return slider.objects.all()


