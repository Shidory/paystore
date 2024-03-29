from django.contrib import admin

from .models import Product, ProductImage, Variation

class ProductAdmin(admin.ModelAdmin):
    # Updated
    date_hierarchy = 'timestamp'
    # Can search now
    search_fields = ['price', 'description']
    list_display = ['title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)