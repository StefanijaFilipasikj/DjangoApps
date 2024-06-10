from django.contrib import admin
from .models import Manufacturer, NutritionalValue, Supplement, ActiveIngredient, ActiveIngredientInSupplement

# Register your models here.


class ActiveIngredientInSupplementInlineAdmin(admin.TabularInline):
    model = ActiveIngredientInSupplement
    extra = 1


class SupplementAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_filter = ('name', 'manufacturer', 'price', 'category')
    inlines = [ActiveIngredientInSupplementInlineAdmin,]
    fieldsets = [
        ('Basic info', {'fields': ['name', 'code', 'image']}),
        ('Details', {'fields': ['manufacturer', 'category', 'price', 'nutritional_value', 'available']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SupplementAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class ActiveIngredientAdmin(admin.ModelAdmin):
    search_fields = ('name', )

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(NutritionalValue)
admin.site.register(Supplement, SupplementAdmin)
admin.site.register(ActiveIngredient, ActiveIngredientAdmin)
