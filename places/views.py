from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place
from django.http import JsonResponse


def home_view(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.coordinates_lng, place.coordinates_lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_details', args=[place.id]),
            },
        })

    context = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'index.html', context={'context': context})

def place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related("images"), id=place_id)
    images = place.images.all()

    response = {
        'title': place.title,
        'imgs': [image.image.url for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinates_lng,
            'lat': place.coordinates_lat,
        }
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 2})