from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from .models import Product, Option, Order
from .mqtt import mqtt_handler



class IndexView(generic.ListView):
    template_name = "shop/index.html"
    context_object_name = "product_list"
    model = Product

    # add the options to the site
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super(IndexView, self).get_context_data(**kwargs)
        context["option_list"] = Option.objects.order_by('name_int')
        return context
    

class CartView(generic.DetailView):
    model = Order
    template_name = "shop/cart.html"


class ReceiptView(generic.ListView):
    model = Order
    template_name = "shop/receipt.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Order.objects.order_by("-order_date")


def select(request):
    '''Gets the data from the selection html form'''

    try:
        selected_product = Product.objects.get(id=request.POST["product"])

        selected_options = []
        for option_id in request.POST.getlist("option"):
            selected_options.append(Option.objects.get(pk=option_id))

    except (KeyError, Product.DoesNotExist):
        # Redisplay the selection form.
        return HttpResponseRedirect(reverse("shop:index"))
    
    else:
        print(selected_product)
        print(selected_options)

        order = Order(order_date=timezone.now())
        order.save()
        order.product.add(selected_product)
        for option in selected_options:
            order.options.add(option)
        order.save()

        return HttpResponseRedirect(reverse("shop:cart", args=(order.id,)))


def order(request, order_id):
    '''Gets the data from the order form'''

    # check if cancel button was pressed an delete order from database
    if request.POST["button"] == "cancel":
        Order.objects.get(id=order_id).delete()
        return HttpResponseRedirect(reverse("shop:index"))
    

    order = Order.objects.get(id=order_id)
    order.order_date = timezone.now()
    order.save()
    # TODO: send order per mqtt

    order_data = {
        "name": order_id,
        "color": order.product.get().product_color,
    }
    for option in order.options.all():
        order_data.update({option.name_int: True})

    mqtt_handler.send_data(order_data)
    print(order_data)
    return HttpResponseRedirect(reverse("shop:receipt", args=(order_id,)))


def reorder(request):
    '''Adds selected order back to cart'''
    
    old_order = Order.objects.get(id=request.POST["button"])
    # create new order with the same content
    order = Order(order_date=timezone.now())
    order.save()
    order.product.add(old_order.product.get())
    for option in old_order.options.all():
        order.options.add(option)
    order.save()

    return HttpResponseRedirect(reverse("shop:cart", args=(order.id,)))
