from django.db import models

# Create your models here.


class array(models.Model):
    boby = models.TextField(blank = True)

    foto = models.ImageField(null = True, blank = True)

    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.boby[0:50]

    class Meta:
        ordering = ['-updated']
