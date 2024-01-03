from django.contrib import admin

# Register your models here.
from .models import Product, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Color of Product", {"fields": ["product_color"], "classes": ["collapse"]}),
    ]
    inlines = [OptionInline]
    list_display = ["name", "product_color"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)