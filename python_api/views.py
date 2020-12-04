from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TdmNhanvien
from .serializers import GetAllAccountSerializer


# Create your views here.
class GetAllAccountAPIView(APIView):
    http_method_names = ['get', 'head']

    def get(self, request):
        list_account = TdmNhanvien.objects.all()
        serializer = GetAllAccountSerializer(list_account, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
