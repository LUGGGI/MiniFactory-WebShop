from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.OptionView.as_view(), name="option"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:product_id>/select/", views.select, name="select"),
]