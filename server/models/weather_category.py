from django.db import models

from server.models.base import BaseModel


class WeatherCategory(BaseModel):
    key = models.CharField(max_length=255)

    class Meta:
        db_table = 'weather_categories'
