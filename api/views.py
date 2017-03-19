from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Miners
from .serializers import MinsersSerializer


# List all miners or create a new one
class MinersList(APIView):

    def get(self, request):
        Miners.objects.all()
        serializer = MinsersSerializer(Miners, many=True)
        return Response(serializer.data)

    def post(self):
        pass
