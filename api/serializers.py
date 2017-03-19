from rest_framework import serializers
from .models import Miners


class MinsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miners
        fields = ('name', 'ip')
