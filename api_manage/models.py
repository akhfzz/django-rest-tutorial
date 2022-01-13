from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=100)
    prodi = models.CharField(max_length=80)
    angkatan = models.IntegerField()
