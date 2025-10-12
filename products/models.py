from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    """Model representing a category of wine."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='wines', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    rating = models.FloatField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
