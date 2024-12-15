from django.db import models

# Create your models here.
class Media(models.Model):

    # class Meta:
    #     verbos_name_plural = "Media"

    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to="media_image")
    url = models.URLField()