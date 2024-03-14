from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("select/", views.select, name="select"),
    path("<int:pk>/cart/", views.CartView.as_view(), name="cart"),
    path("<int:order_id>/order/", views.order, name="order"),
    path("<int:pk>/receipt/", views.ReceiptView.as_view(), name="receipt"),
    path("reorder/", views.reorder, name="reorder"),
]