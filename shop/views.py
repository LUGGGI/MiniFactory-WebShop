from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product, Option


class IndexView(generic.ListView):
    template_name = "shop/index.html"

    def get_queryset(self):
        """Return the last five published products (not including those set to be published in the future)."""
        return Product.objects.order_by("name")
    
class OptionView(generic.DetailView):
    model = Product
    template_name = "shop/option.html"

    def get_queryset(self):
        """
        Excludes any products that aren't published yet.
        """
        return Product.objects.order_by("name")
    

class ResultsView(generic.DetailView):
    model = Product
    template_name = "shop/results.html"
    

def select(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        selected_options = []
        for option_id in request.POST.getlist("option"):
            selected_options.append(product.option_set.get(pk=option_id))
        print(selected_options)
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
        for option in selected_options:
            option.selections += 1
            option.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("shop:results", args=(product.id,)))