from django.db import models
from historicos.models import Historicos
from pacientes.models import Pacientes

def imagens_historico(instance, filename):
    return '/'.join(['historico', str(instance.id_historico.id_historico), filename])

def imagens_paciente(instance, filename):
    return '/'.join(['paciente', str(instance.id_paciente.id_paciente), filename])

class ImagensHistorico(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)
    imagem = models.ImageField(blank=True, null=True, upload_to=imagens_historico)
    id_historico = models.ForeignKey(Historicos, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)

class ImagensPaciente(models.Model):
    id_imagem_paciente = models.AutoField(primary_key=True)
    imagem = models.ImageField(blank=True, null=True, upload_to=imagens_paciente)
    id_paciente = models.ForeignKey(Pacientes, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)
