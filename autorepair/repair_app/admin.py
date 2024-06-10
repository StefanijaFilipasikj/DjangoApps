from django.contrib import admin
from .models import Manufacturer, Automobile, RepairShop, Repair, RepairShopManufacturer
# Register your models here.


class RepairShopManufacturerInlineAdmin(admin.TabularInline):
    model = RepairShopManufacturer
    extra = 0


class RepairShopAdmin(admin.ModelAdmin):
    inlines = [RepairShopManufacturerInlineAdmin,]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class RepairAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RepairAdmin, self).save_model(request, obj, form, change)


class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('type', 'max_speed',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Automobile, AutomobileAdmin)
admin.site.register(RepairShop, RepairShopAdmin)
admin.site.register(Repair, RepairAdmin)
