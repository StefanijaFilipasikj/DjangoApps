from django.contrib import admin
from .models import Band, Event, BandInEvent


class BandInEventInlineAdmin(admin.TabularInline):
    model = BandInEvent
    extra = 0


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    exclude = ('user', 'bands', 'number_of_bands')
    inlines = [BandInEventInlineAdmin,]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.number_of_bands = 0
        super(EventAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    exclude = ('num_events',)

    def save_model(self, request, obj, form, change):
        obj.num_events = 0
        super(BandAdmin, self).save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Band, BandAdmin)
admin.site.register(Event, EventAdmin)
