from django.contrib import admin
from .models import Country, Brand, Product, StoreLocation, ProductInStore
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(self, ProductAdmin).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False



class ProductInStoreInlineAdmin(admin.TabularInline):
    model = ProductInStore
    extra = 1


class StoreLocationAdmin(admin.ModelAdmin):
    inlines = [ProductInStoreInlineAdmin,]


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Country, CountryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(StoreLocation, StoreLocationAdmin)
