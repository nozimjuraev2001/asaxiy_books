from django.contrib import admin
from . import models

@admin.register(models.AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(models.BookImageModel)
class BookImageAdmin(admin.ModelAdmin):
    pass
@admin.register(models.FeaturesModel)
class FeaturesModelAdmin(admin.ModelAdmin):
    pass
@admin.register(models.PublisherModel)
class PublisherModelAdmin(admin.ModelAdmin):
    pass
@admin.register(models.TranslatorModel)
class TranslatorModelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    readonly_fields = ['real_price']