from django.contrib import admin
from .models import PublishingHouse, Book, Author, BookAuthor, PublishingHouseAuthor

# Register your models here.


class BookAuthorInlineAdmin(admin.TabularInline):
    model = BookAuthor
    extra = 1


class PublishingHouseAuthorInlineAdmin(admin.StackedInline):
    model = PublishingHouseAuthor
    extra = 1


class BookAdmin(admin.ModelAdmin):
    exclude = ('user',)
    inlines = [BookAuthorInlineAdmin,]
    search_fields = ('title',)
    list_filter = ('title', 'publishing_house__name', 'category')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BookAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class AutorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInlineAdmin, PublishingHouseAuthorInlineAdmin]
    search_fields = ('name', 'surname')

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


admin.site.register(PublishingHouse)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AutorAdmin)

