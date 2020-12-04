from rest_framework import serializers
from .models import TdmNhanvien


class GetAllAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TdmNhanvien
        fields = ['manv', 'tennv', 'mato']

    pass
