from django.db import models


class categories(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
# Create your models here.
class products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=120)
    categories = models.ForeignKey(categories, null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default=0, blank=False, null=False)
    stock = models.DecimalField(max_digits=10000, decimal_places=0, default=1, blank=False, null=False)
    weight = models.DecimalField(max_digits=10000, decimal_places=2, default=0.0, blank=False, null=False)

