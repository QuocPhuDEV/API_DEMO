from rest_framework import serializers
from .models import TdmNhanvien
from .models import TdmKho


class GetAllAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TdmNhanvien
        fields = ['ngaytao', 'usertao', 'ngaycn', 'usercn', 'tennv']

    pass


class GetDataKho(serializers.ModelSerializer):
    class Meta:
        model = TdmKho
        files = ['makho', 'tenkho']
        pass
