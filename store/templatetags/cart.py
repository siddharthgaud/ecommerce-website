from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(i,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        print(id,i.id)
        print(type(id),type(i.id))
        if int(id) == i.id:
            return True
    print("product:",i,"cart:",cart)
    return False


@register.filter(name="cart_quantity")
def cart_quantity(i,cart):
    keys = cart.keys()
    # print(keys)
    for id in keys:
        # print(id,i.id)
        # print(type(id),type(i.id))
        if int(id) == i.id:
            return cart.get(id)
    print("product:",i,"cart:",cart)
    return 0

@register.filter(name="price_total")
def price_total(p,cart):
    return p.price * cart_quantity(p,cart)

@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total (p, cart)#sum=sum+

    return sum