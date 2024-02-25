from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("option/", views.OptionView.as_view(), name="option"),
    path("select_options/", views.select_options, name="select_options"),
    path("select_product/", views.select_product, name="select_product"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]