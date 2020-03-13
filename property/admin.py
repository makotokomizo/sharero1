from django.contrib import admin

# Register your models here.
from .models import Property, Category, Reserve, SharableItem

class PropertyAdmin(admin.ModelAdmin):
    # list_display = ['lastName', 'firstName', 'property_type', 'category', 'area', 'beds_number', 'garages_number', 'location']
    list_display = ['user', 'lastName', 'firstName', 'property_type', 'category', 'beds_number', 'location']
    search_fields = ['lastName', 'firstName', 'property_type']
    list_filter = ['category', 'property_type']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)
admin.site.register(SharableItem)