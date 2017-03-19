from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Miners, Heartbeat
from .serializers import MinsersSerializer, HeartbeatSerializer


# List all miners or create a new one
class MinersList(APIView):
    def get(self, request):
        queryset = Miners.objects.all()
        serializer = MinsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class HeartbeatList(APIView):
    def get(self):
        pass

    def post(self, request):
        serializer = HeartbeatSerializer(Heartbeat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
