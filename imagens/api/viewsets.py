from rest_framework import viewsets

from imagens.models import ImagensHistorico, ImagensPaciente
from imagens.api.serializers import ImagensHistoricoSerializer, ImagensPacienteSerializer

class ImagensHistoricoViewSet(viewsets.ModelViewSet):
    queryset = ImagensHistorico.objects.all()
    serializer_class = ImagensHistoricoSerializer

class ImagensPacienteViewSet(viewsets.ModelViewSet):
    queryset = ImagensPaciente.objects.all()
    serializer_class = ImagensPacienteSerializer