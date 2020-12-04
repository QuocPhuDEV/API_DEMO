from django.db import models


# Create your models here.
class TdmNhanvien(models.Model):
    ngaytao = models.DateField(blank=True, null=True)
    usertao = models.CharField(max_length=10, blank=True, null=True)
    ngaycn = models.DateField(blank=True, null=True)
    usercn = models.CharField(max_length=10, blank=True, null=True)
    manv = models.CharField(primary_key=True, max_length=10)
    tennv = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    groupid = models.CharField(max_length=10, blank=True, null=True)
    mato = models.CharField(max_length=10, blank=True, null=True)
    trangthai = models.BooleanField(blank=True, null=True)
    skin = models.CharField(max_length=50, blank=True, null=True)
    lang = models.CharField(max_length=10, blank=True, null=True)
    manvql = models.CharField(max_length=10, blank=True, null=True)
    machucvu = models.CharField(max_length=2, blank=True, null=True)
    qrlogin = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tdm_nhanvien'
