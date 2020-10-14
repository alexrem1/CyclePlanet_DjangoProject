from django.db import models


class bike_type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class condition(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class deals(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class product(models.Model):
    brand = models.ForeignKey('brand', null=True, blank=True, on_delete=models.SET_NULL)
    deals = models.ForeignKey('deals', null=True, blank=True, on_delete=models.SET_NULL)
    bike_type = models.ForeignKey('bike_type', null=True, blank=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey('condition', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=254)
    SKU = models.IntegerField()
    seller_notes = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_was = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    photo_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    wheel_size = models.TextField()
    color = models.TextField()
    gender = models.TextField()
    Type = models.TextField()
    size = models.TextField()
    number_of_speeds = models.TextField()        

    def __str__(self):
        return self.name