from rest_framework import serializers

from imagens.models import ImagensHistorico, ImagensPaciente

class ImagensHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensHistorico
        fields = '__all__'

class ImagensPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensPaciente
        fields = '__all__'
