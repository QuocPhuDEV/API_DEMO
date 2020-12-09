from rest_framework import serializers
from .models import TdmNhanvien
from .models import TdmKho


class GetAllAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TdmNhanvien
        fields = ['manv', 'tennv', 'mato']

    pass


class GetDataKho(serializers.ModelSerializer):
    class Meta:
        model = TdmKho
        files = ['makho', 'tenkho']
        pass
