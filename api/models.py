from django.db import models


# Create your models here.

class Miners(models.Model):
    name = models.CharField(max_length=16)
    ip = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Heartbeat(models.Model):
    name = Miners.name
    time = models.DateTimeField()

    def __str__(self):
        return self.name
