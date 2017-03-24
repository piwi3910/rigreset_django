from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Miners, Heartbeat, test
from .serializers import MinersSerializer, HeartbeatSerializer, testSerializer


# List all miners or create a new one
class MinersList(APIView):
    def get(self, request):
        queryset = Miners.objects.all()
        serializer = MinersSerializer(queryset, many=True)
        return Response(serializer.data)


class HeartbeatList(APIView):
    def get(self,request):
        queryset = Heartbeat.objects.all()
        serializer = HeartbeatSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeartbeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class testList(APIView):
    def get(self,request):
        queryset = test.objects.all()
        serializer = testSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = testSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)