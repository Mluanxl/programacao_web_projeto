from django.db import models

class Usuario(models.Model):
    PERFIS = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('organizador', 'Organizador'),
    ]

    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    instituicao = models.CharField(max_length=50)
    usuario_login = models.CharField(max_length=25, unique=True)
    senha = models.CharField(max_length=25)
    perfil = models.CharField(max_length=15, choices=PERFIS)

    def __str__(self):
        return f"{self.nome} ({self.perfil})"
