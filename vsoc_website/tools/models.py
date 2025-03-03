from django.db import models

class Tools_main(models.Model):
    name = models.CharField('Tool Name', max_length=60)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    Documentation = models.URLField(blank=True)

    def __str__(self):
        return self.name
