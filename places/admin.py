from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from places.models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 0
    fields = ('image', 'image_tag', 'position')
    readonly_fields = ('image_tag',)
    list_filter = ['title']
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    sortable_field = 'position'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'coordinates_lat', 'coordinates_lng')
    inlines = [PlaceImageInline]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'image_tag')
    list_filter = ['title']
    readonly_fields = ('image_tag',)

