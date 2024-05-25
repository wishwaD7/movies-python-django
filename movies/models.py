from django.db import models

class Movie(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f'{self.id} {self.title} {self.year} {self.rating}'
