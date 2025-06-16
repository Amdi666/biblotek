from django.db import models

class Libri(models.Model):
    titulli = models.CharField(max_length=200)
    autori = models.CharField(max_length=100)
    viti_publikimit = models.IntegerField()

    def __str__(self):
        return self.titulli


