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


class TdmKho(models.Model):
    ngaytao = models.DateField(blank=True, null=True)
    usertao = models.CharField(max_length=10, blank=True, null=True)
    ngaycn = models.DateField(blank=True, null=True)
    usercn = models.CharField(max_length=10, blank=True, null=True)
    makho = models.CharField(primary_key=True, max_length=10)
    mapx = models.CharField(max_length=10, blank=True, null=True)
    malk = models.CharField(max_length=10, blank=True, null=True)
    tenkho = models.CharField(max_length=150, blank=True, null=True)
    diengiai = models.CharField(max_length=300, blank=True, null=True)
    qltl = models.CharField(max_length=1, blank=True, null=True)
    manhomkho = models.CharField(max_length=10, blank=True, null=True)
    tkkd = models.CharField(max_length=1, blank=True, null=True)
    tksxpx = models.CharField(max_length=1, blank=True, null=True)
    huyplt = models.CharField(max_length=1, blank=True, null=True)
    xemtkmobile = models.CharField(max_length=1, blank=True, null=True)
    dhnd = models.CharField(max_length=1, blank=True, null=True)
    dhxk = models.CharField(max_length=1, blank=True, null=True)
    sxtk = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDM_KHO'
