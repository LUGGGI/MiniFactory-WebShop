from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    product_color = models.CharField(max_length=5, choices=(("White", "White"), ("Red", "Red"), ("Blue", "Blue")))

    def __str__(self) -> str:
        return self.name


class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=50)
    selections = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.option_text