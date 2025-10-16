from django.db import models
from usuarios.models import Usuario

class Evento(models.Model):
    TIPOS = [
        ('seminario', 'Seminário'),
        ('palestra', 'Palestra'),
        ('monitoria', 'Monitoria'),
    ]

    tipo = models.CharField(max_length=25, choices=TIPOS)
    titulo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} : {self.tipo}"

class Inscricao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} : {self.evento}"

class Certificado(models.Model):
    inscricao = models.OneToOneField('Inscricao', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    emitido_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificado {self.codigo}"

