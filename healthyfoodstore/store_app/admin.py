from django.contrib import admin
from .models import Category, Client, Product, Order, ProductInOrder

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class ProductInlineAdmin(admin.TabularInline):
    model = Product
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductInlineAdmin,]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ClientAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name', 'surname')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ClientAdmin, self).save_model(request, obj, form, change)


class ProductInOrderInlineAdmin(admin.TabularInline):
    model = ProductInOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInlineAdmin,]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
