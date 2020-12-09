from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TdmNhanvien
from .serializers import GetAllAccountSerializer

from django.db import connection
from django.shortcuts import render
import cx_Oracle


# Create your views here.
class GetAllAccountAPIView(APIView):
    http_method_names = ['get', 'head']

    # Lấy tất cả dữ liệu (none sql)
    # def get(self, request):
    #     list_account = TdmNhanvien.objects.all()
    #     serializer = GetAllAccountSerializer(list_account, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # Lấy tất cả dữ liệu (có sql nhưng không Serialier)
    # def get(self, request):
    #     cursor = connection.cursor()
    #     sql = "select * from tdm_nhanvien"
    #     list_account = cursor.execute(sql)
    #     serializer = GetAllAccountSerializer(list_account, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # Lấy tất cả dữ liệu (có sql và sử dụng Serialier)
    def get(self, request):
        sql = "select * from tdm_nhanvien"
        list_account = TdmNhanvien.objects.raw(sql)
        serializer = GetAllAccountSerializer(list_account, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # Gọi procedure không tham số
    def callNewUser(request):
        cursor = connection.cursor()
        ref = cursor.callproc("DJ_PHU_TEST1")
        cursor.close()
        return ref

    # Gọi pro có tham số
    def callNewUserWithParam(selt, maNV, tenVN):
        cursor = connection.cursor()
        manv = cursor.arrayvar(cx_Oracle.STRING, maNV)
        manv = cursor.arrayvar(cx_Oracle.STRING, maNV)
        ref = cursor.callproc("DJ_PHU_TEST2", [manv, tenVN])
        cursor.close()
        return ref
