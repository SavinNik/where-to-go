from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0
    fields = ('image', 'position')
    readonly_fields = ()


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates_lat', 'coordinates_lng')
    inlines = [PlaceImageInline]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'position')
    list_filter = ['title']

