from django.db import models
from django.contrib.auth.models import User


class bike_type(models.Model):

    class Meta:
        verbose_name_plural = "Bike Type"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class brand(models.Model):

    class Meta:
        verbose_name_plural = "Brand"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class condition(models.Model):

    class Meta:
        verbose_name_plural = "Condition"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class deals(models.Model):

    class Meta:
        verbose_name_plural = "Deals"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    brand = models.ForeignKey(
        'brand', null=True, blank=True, on_delete=models.SET_NULL)
    deals = models.ForeignKey(
        'deals', null=True, blank=True, on_delete=models.SET_NULL)
    bike_type = models.ForeignKey(
        'bike_type', null=True, blank=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey(
        'condition', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=254)
    SKU = models.IntegerField()
    seller_notes = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_was = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    photo_url = models.URLField(max_length=1024, default='', blank=True)
    image = models.ImageField(default='', blank=True)

    wheel_size = models.TextField()
    color = models.TextField()
    gender = models.TextField()
    Type = models.TextField()
    size = models.TextField()
    number_of_speeds = models.TextField()

    def __str__(self):
        return self.name


class ProductReview(models.Model):

    class Meta:
        verbose_name_plural = "Product Review"

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=750)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name
