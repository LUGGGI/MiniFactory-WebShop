from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from .models import Product, Option, Order




class IndexView(generic.ListView):
    model = Product
    template_name = "shop/index.html"

    # def get_queryset(self):
    #     return Product.objects.order_by("name")
    
class OptionView(generic.DetailView):
    model = Product
    template_name = "shop/option.html"

    # def get_queryset(self):
    #     """
    #     Excludes any products that aren't published yet.
    #     """
    #     return Product.objects.order_by("name")
    

class ResultsView(generic.DetailView):
    template_name = "shop/results.html"

    def get_queryset(self):
        """
        Excludes any products that aren't published yet.
        """
        return Order.objects.order_by("order_date")
    

def select(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        order_number = Order.objects.latest("order_date").number + 1

        json_data = {
            "name": f"nr{order_number}",
            "color": product.product_color
        }

        for option in product.options.all():
            json_data.update({option.name_int: False})

        for option_id in request.POST.getlist("option"):
            json_data.update({product.options.get(pk=option_id): True})
        print(json_data)
    except Exception as e:
        # Redisplay the product select form.
        return render(
            request,
            "shop/option.html",
            {
                "product": product,
                "error_message": f"Error: {e}",
            },
        )
    else:
        
        
        order = Order(number=order_number, order_date=timezone.now())
        order.save()
        order.products.add(product)
        order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("shop:results", args=(order.id,)))