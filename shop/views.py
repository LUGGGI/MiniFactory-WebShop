from typing import Any
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from .models import Product, Option, Order




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
    

    Order.objects.get(id=order_id).order_date = timezone.now()
    # TODO: send order per mqtt

    return HttpResponseRedirect(reverse("shop:receipt", args=(order_id,)))