from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание')
    coordinates_lat = models.FloatField(verbose_name='Широта')
    coordinates_lng = models.FloatField(verbose_name='Долгота')

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(upload_to='place_images' ,verbose_name='Изображение', db_index=True)
    position = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Позиция')

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


