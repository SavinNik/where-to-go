from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpRequest


def home_view(request: HttpRequest):
    return HttpResponse("<h1>Здесь будет карта</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home')
]
