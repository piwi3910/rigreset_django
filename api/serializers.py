from rest_framework import serializers
from .models import Miners, Heartbeat


class MinersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miners
        fields = ('id', 'name', 'ip', 'status')


class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ('id', 'time')
