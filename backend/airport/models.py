from django.db import models

class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10)
    position = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.airport_code