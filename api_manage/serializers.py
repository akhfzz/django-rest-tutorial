from rest_framework import serializers
from .models import Mahasiswa

class MahasiswaForm(serializers.ModelSerializer):
    nim = serializers.IntegerField()
    nama = serializers.CharField(max_length=100)
    prodi = serializers.CharField(max_length=80)
    angkatan = serializers.IntegerField()

    class Meta:
        model = Mahasiswa
        fields = ('__all__')