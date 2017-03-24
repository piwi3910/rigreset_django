from django.db import models
import uuid


# Create your models here.
class Miner_status(models.Model):
    key = models.AutoField(primary_key=True)
    status = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.status


class Miners(models.Model):
    key = models.AutoField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=16, unique=True)
    ip = models.CharField(max_length=16, unique=True)
    status = models.ForeignKey(Miner_status, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Heartbeat(models.Model):
    key = models.AutoField(primary_key=True)
    id = models.ForeignKey(Miners, to_field='id', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time)


class test(models.Model):
    name = models.CharField(max_length=16)
    data = models.CharField(max_length=16)

    def __str__(self):
        return self.name
