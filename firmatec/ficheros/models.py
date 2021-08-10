from django.db import models

# Create your models here.
"""Django models utilities."""

import os
# Django
# from django.db import models
from django.core.validators import FileExtensionValidator
#Utilities
from utils.models import BaseModel, Planta


class Fichero(BaseModel):
    """Fichero Model

    El objeto Fichero tiene los siguientes atributos:
        + nombre (char): Nombre del Fichero
        + desc (text): Descripcion del Fichero
        + archivo (file): Atributo con la referencia al achivo
        + plantas (manytomony): Las plantas que pueden visualizar este fichero.
        + activo (boolean): Estado del Fichero.
    """

    activo = models.BooleanField(
        default=True,
        help_text='Para desactivar la publicación de este fichero, deshabilite esta casilla.'
    )

    archivo = models.FileField(
        upload_to='ficheros/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg', ])]
    )

    desc = models.TextField(
        'Descripción',
        blank=True,
        null=True
    )

    nombre = models.CharField(
        max_length=120,
    )

    plantas = models.ManyToManyField(Planta)

    def __str__(self):
        return self.nombre

    @property
    def nombre_archivo(self):
        return os.path.basename(self.archivo.name)

    @property
    def extension_archivo(self):
        name, extension = os.path.splitext(self.archivo.name)
        return extension

