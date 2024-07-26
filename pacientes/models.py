from django.db import models 

# Atributos do pacienteS
class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rg =  models.CharField(max_length=100, blank=True, null=True)

# Configurações para o banco de dados - poderá ser manipulada e seu nome
class Meta:
    managed = True
    db_table = 'pacientes'