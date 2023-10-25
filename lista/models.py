from django.db import models

class item(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item
# Create your models here.
