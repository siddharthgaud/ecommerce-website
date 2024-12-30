from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Customer
from store.models import Products
from store.models import Category
from store.models import slider
from django.views import View
from datetime import datetime


class Index(View):
    def post(self,request):
        product = request.POST.get('product')       # add to cart functionality
        remove = request.POST.get('remove')       
        print("ID=", product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            print("quantity:",quantity)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                     cart[product] = quantity + 1    
            else:
                cart[product] =  1    
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart:",cart)   
        return redirect('homepage')
        
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # request.session.get('cart').clear()
        # request.session.clear()
        # display all products and categories and filter products according to category selected
        slide = slider.get_all_sliders()
        products = Products.get_all_products()
        categories = Category.get_all_categories()
        print("products:",products)
        print("categories:",categories)

        category_id = request.GET.get('category')
        print("category_id:",category_id)

        if category_id:
            products = Products.get_all_products_by_categoryid(category_id)
        else:
            products = Products.get_all_products()    

        data = {
            'products':products,
            'categories':categories,
            'slider':slide
        }
        print("your customer id:",request.session.get('id'))     # session handling
        print("your email:",request.session.get('email'))
    
        return render(request,'index.html',data)
     



    

#######################################################################################################


def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('pw')
        print(email,password)
        customer=Customer.get_customer_by_email(email)
        print("info:",customer)
        if customer:
            if password == customer.password:
                print("login")
                request.session['id'] = customer.id
                print("customer_id:",customer.id)
                # request.session['email'] = customer.email
                print("customer.email:",customer.email)

                return redirect('homepage')

            else:
                print("NOT LOGIN")           
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    

    
##########################################################################################################


def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        pw=request.POST['pw']
        cust=Customer(first_name=fname,last_name=lname,phone=phone,email=email,password=pw)
        cust.save()
        return redirect('/login')
    else:
        return render(request,'signup.html')

def logout(request):
    request.session.clear()
    return redirect("login")


def cart(request):
    ids = list(request.session.get('cart').keys())  # all ids
    products = Products.get_products_by_id(ids)
    print(products)
    return render(request, 'cart.html',{'products':products})




def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


################################################################################################




