from django.db import models


class ProductLine(models.Model):
    productLineName = models.CharField(max_length=40)

    def __str__(self):
        return self.productLineName


class Product(models.Model):
    productName = models.CharField(max_length=40)
    ProdLine = models.ForeignKey(
        ProductLine, on_delete=models.PROTECT)

    def __str__(self):
        return self.productName


class Feature(models.Model):
    featureName = models.CharField(max_length=40)
    prodParent = models.ForeignKey(
        Product, verbose_name=("Product Parent"), on_delete=models.PROTECT)

    def __str__(self):
        return self.featureName
