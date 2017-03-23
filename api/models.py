from django.db import models
import uuid


# Create your models here.

class Miners(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16)
    ip = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Heartbeat(models.Model):
    name = Miners.name
    time = models.DateTimeField()

    def __str__(self):
        return self.name
