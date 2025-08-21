from django.contrib import admin
from .models import Category, Wine



# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name', 
        'category',
        'description',
        'slug',
        'wines_count',
        'price',
        'image'
)


class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


admin.site.register(Category)
admin.site.register(Wine)

