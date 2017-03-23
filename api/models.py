from django.db import models
import uuid


# Create your models here.

class Miners(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16, unique=True)
    ip = models.CharField(max_length=16, unique=True)
    status = models.CharField(max_length=1, default=1, editable=False)

    def __str__(self):
        return self.name


class Heartbeat(models.Model):
    key = models.AutoField(primary_key=True)
    id = models.OneToOneField(Miners, on_delete=models.CASCADE)
    time = models.DateTimeField()

    #def __str__(self):
     #   return self.key
