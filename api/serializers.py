from rest_framework import serializers
from .models import Miners, Heartbeat


class MinsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miners
        fields = ('name', 'ip')


class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ('name', 'time')
