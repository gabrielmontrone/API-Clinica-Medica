from rest_framework import serializers

from pacientes.models import Pacientes
from agendamentos.api.serializers import AgendamentosDetalhesSerializer
class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__' # Importar todos os campos de models.py

class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'data_nascimento',
            'endereco',
            'num_endereco',
            'bairro_endereco',
            'cep',
            'data_cadastro',
            'rg',
            'agendamentos'
        ]