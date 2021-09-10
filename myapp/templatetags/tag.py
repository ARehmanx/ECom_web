from django import template
import math
from myapp.models import Products, Cart

register = template.Library()


@register.simple_tag
def percentage_cal1(x):
    global a
    a = x
    return a


@register.simple_tag
def percentage_cal2(y):
    global b
    b = y
    return b


@register.simple_tag
def percentage_cal3():
    z = ((a - b) / a) * 100

    return math.trunc(z)


@register.simple_tag
def product_counters(c, br):
    p = Products.objects.filter(categories__category=c, brands=br)
    return len(p)


@register.simple_tag
def number_of_star(s):
    y = []
    for x in range(s):
        y.append(x)
    return y


@register.simple_tag
def product_quantity(tp,p):
    w = tp/p
    return math.trunc(w)
