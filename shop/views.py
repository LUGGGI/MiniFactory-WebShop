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
    
class OptionView(generic.ListView):
    model = Option
    template_name = "shop/option.html"

    # def get_queryset(self):
    #     """
    #     Excludes any products that aren't published yet.
    #     """
    #     return Product.objects.order_by("name")
    

class ResultsView(generic.DetailView):
    model = Product
    template_name = "shop/results.html"

    # def get_queryset(self):
    #     """
    #     Excludes any products that aren't published yet.
    #     """
    #     return Order.objects.order_by("order_date")
    

def select_options(request):
    try:
        # order_number = Order.objects.latest("order_date").number + 1

        selected_options = []

        for option_id in request.POST.getlist("option"):
            selected_options.append({Option.objects.get(pk=option_id): True})
        
    except Exception as e:
        # Redisplay the product select form.
        return render(
            request,
            "shop/option.html",
            {
                "option": Option,
                "error_message": f"Error: {e}",
            },
        )
    else:
        print(selected_options)
        
        # order = Order(number=order_number, order_date=timezone.now())
        # order.save()
        # order.products.add(product)
        # order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("shop:results", args=(1,)))
    

def select_product(request):
    # product = get_object_or_404(Product, pk=product_id)
    try:
        pk = request.POST["product"]
        selected_product = Product.objects.get(id=pk)
        # selected_product = product.choice_set.get(pk=request.POST["product"])
    except (KeyError, Product.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "shop.html",
            {
                "product": Product,
                "error_message": "You didn't select a product.",
            },
        )
    else:
        print(pk, selected_product)
        # selected_choice.votes += 1
        # selected_choice.save()
        # # Always return an HttpResponseRedirect after successfully dealing
        # # with POST data. This prevents data from being posted twice if a
        # # user hits the Back button.
        return HttpResponseRedirect(reverse("shop:results", args=(pk,)))