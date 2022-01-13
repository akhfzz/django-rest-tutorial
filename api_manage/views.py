from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MahasiswaForm
from .models import Mahasiswa 

# Create your views here.
class APIMahasiswa(APIView):
    def post(self, request):
        pharser = MahasiswaForm(data=request.data)
        if pharser.is_valid():
            pharser.save()
            return Response(
                {
                    'status': 200,
                    'message': 'Sudah kami simpan',
                    'data': pharser.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'status': 400,
                    'message': 'Cek kembali erornya',
                    'data': pharser.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, id=None):
        if id:
            item = Mahasiswa.objects.get(id=id)
            serializer = MahasiswaForm(item)
            return Response({
                'status': 200,
                'message': 'Data tersedia',
                'data': serializer.data 
            },
            status=status.HTTP_200_OK)
        items = Mahasiswa.objects.all()
        serializer = MahasiswaForm(items, many=True)
        # print(items)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Mahasiswa.objects.get(id=id)
        pharser = MahasiswaForm(item, partial=True, data=request.data)
        if pharser.is_valid():
            pharser.save()
            return Response(
                {
                    'status': 200,
                    'message': 'berhasil diubah',
                    'data': pharser.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'status': 400,
                    'message': 'Tidak tersedia data',
                    'data': pharser.errors
                }
            )
        
    def delete(self, request, id=None):
        item = get_object_or_404(Mahasiswa, id=id)
        item.delete()
        return Response(
            {
                'status': 200,
                'message': 'data dihapus'
            },
            status=status.HTTP_200_OK
        )