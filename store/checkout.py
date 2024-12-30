from django.shortcuts import render , redirect
from .models import Customer
from django.views import View
from .models import Products
from .models import Order

class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('id')    #id customer id

        cart = request.session.get('cart')#cart from session
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)


        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return render(request,'cart.html')
        










        # address = request.POST.get('address')
        # phone = request.POST.get('phone')
        # customer = request.session.get('customer')    #id customer id

        # cart = request.session.get('cart')#cart from session
        # products = Products.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)


        # for product in products:
        #     print(cart.get(str(product.id)))
        #     order = Order(customer=Customer(id=customer),
        #                   product=product,
        #                   price=product.price,
        #                   address=address,
        #                   phone=phone,
        #                   quantity=cart.get(str(product.id)))
        #     order.save()
        # request.session['cart'] = {}

        # return render(request,'cart.html')