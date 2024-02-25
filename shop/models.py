from django.db import models

# Create your models here.



class Option(models.Model):
    display_text = models.CharField(max_length=50)
    name_int = models.CharField(max_length=50)
    selected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.display_text
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_color = models.CharField(max_length=5, choices=(("WHITE", "White"), ("RED", "Red"), ("BLUE", "Blue")))
    options = models.ManyToManyField(Option)

    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    data = models.JSONField()

    number = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField("date ordered")