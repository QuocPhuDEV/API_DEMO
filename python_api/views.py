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

    # def get(self, request):
    #     list_account = TdmNhanvien.objects.all()
    #     serializer = GetAllAccountSerializer(list_account, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get(self, request):
        cursor = connection.cursor()
        sql = "select * from TDM_NHANVIEN"
        data = cursor.execute(sql)
        return Response(data=data, status=status.HTTP_200_OK)

    # Gọi procedure không tham số
    def callNewUser(request):
        cursor = connection.cursor()
        # cursor.execute("call DJ_PHU_TEST1()")
        # results = cursor.fetchall()
        # return render(request, {'GetDataKho': results})
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
