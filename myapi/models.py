from django.db import models

# Create your models here.
class sensor(models.Model):
    temp = models.CharField(max_length=60)
    ic = models.CharField(max_length=60)
    dist =  models.CharField(max_length=60)
    def __str__(self):
        return self.temp
        return self.id
        return self.dist
