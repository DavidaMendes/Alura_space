from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Aqui cria classes para traduzir para lista de banco de dados 

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALÁXIA", "Galáxia"),
        ("ESTRELA", "Estrela"),
        ("PLANETA", "Planeta"),
    ]

    # Classe Model que representa uma lista de banco de dados
    nome = models.CharField(max_length=100, null=False, blank= False)
    legenda = models.CharField(max_length=100, null=False, blank= False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False, default='')
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        # Parametro caso o usuario seja excluido
        null=True,
        blank=False,
        related_name="user",

    )

    def __str__(self):
        return self.nome

