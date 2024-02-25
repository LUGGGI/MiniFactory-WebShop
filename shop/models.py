from django.db import models

# Create your models here.



class Option(models.Model):
    display_text = models.CharField(max_length=50)
    name_int = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.display_text
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_color = models.CharField(max_length=5, choices=(("WHITE", "White"), ("RED", "Red"), ("BLUE", "Blue")))

    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    product = models.ManyToManyField(Product)
    options = models.ManyToManyField(Option)

    order_date = models.DateTimeField("date ordered")