# Generated by Django 5.0.7 on 2024-07-18 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aparecimentos_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('local_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('conclusao', models.TextField(blank=True, null=True)),
                ('id_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='agendamentos.agendamentos')),
            ],
            options={
                'db_table': 'historicos',
                'managed': True,
            },
        ),
    ]
