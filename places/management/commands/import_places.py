import os
import json
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage
import requests
from io import BytesIO
from django.core.files.images import ImageFile
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Import places data from JSON files'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Path to directory containing JSON files')

    def handle(self, *args, **options):
        directory = options['directory']
        import_test_data_to_db(directory)


def import_test_data_to_db(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    place, created = Place.objects.get_or_create(
                        title=data['title'],
                        description_short=data['description_short'],
                        description_long=data['description_long'],
                        coordinates_lat=data['coordinates']['lat'],
                        coordinates_lng=data['coordinates']['lng'],
                    )

                    for i, url in enumerate(data['imgs'], start=1):
                        try:
                            response = requests.get(url)
                            response.raise_for_status()
                            
                            filename = os.path.basename(urlparse(url).path)
                            image_file = ImageFile(BytesIO(response.content), name=filename)
                            
                            PlaceImage.objects.create(
                                title=place,
                                image=image_file,
                                position=i,
                            )
                        except requests.exceptions.RequestException as e:
                            print(f"Failed to download image {url}: {e}")
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON file {file_path}: {e}")
