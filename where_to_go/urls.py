from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from places.views import home_view, place_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('places/<int:place_id>', place_details, name='place_details')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)