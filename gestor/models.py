from django.db import models

# Create your models here.
class Tarea(models.Model):
    estado = [('terminado','Tarea finalizda'),
            ('incompleto','Tarea incompleta')
            ]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.CharField(max_length=100,choices=estado,default='incompleto')
    def __str__(self):
        return self.titulo
