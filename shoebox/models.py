from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    shoe_type = [
      ('Sneaker', 'Sneaker'),
      ('Boot', 'Boot'),
      ('Sandel', 'Sandel'),
      ('Dress', 'Dress'),
      ('Sneaker', 'Sneaker'),
      ('Other', 'Other'),
    ]
    style = models.CharField(max_length=50, choices=shoe_type)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    colors = [
      ('Red', 'Red'),
      ('Orange', 'Orange'),
      ('Yellow', 'Yellow'),
      ('Green', 'Green'),
      ('Blue', 'Blue'),
      ('Indigo', 'Indigo'),
      ('Violet', 'Violet'),
      ('White', 'White'),
      ('Black', 'Black')
    ]
    color_name = models.CharField(max_length=10, choices=colors)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, related_name='color', on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, related_name='shoe_type', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name-self.manufacturer
