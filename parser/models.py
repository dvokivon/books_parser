from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    availability = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
