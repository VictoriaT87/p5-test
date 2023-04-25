from django.db import models

# Create your models here.


class Product(models.Model):
    app_id = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    date_release = models.DateField()
    description = models.TextField()
    price_final = models.DecimalField(max_digits=6, decimal_places=2)
    price_original = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    steam_deck = models.BooleanField()

    def __str__(self):
        return self.name


class Games(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    brand = models.CharField(max_length=254, default="N/A")
    product_type = models.CharField(max_length=254, default="N/A")
    game_platform = models.CharField(max_length=254, default="N/A")
    operating_systems = models.CharField(max_length=254, default="N/A")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    average_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
