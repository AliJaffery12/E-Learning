from django import template
from django.http import HttpResponse
register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(cat,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==cat.id:
            return True
    return False 

@register.filter(name='cart_quantity')
def cart_quantity(cat,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==cat.id:
            return cart.get(id)
    
    return "purchase this course"