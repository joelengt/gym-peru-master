from django.db import models


class Servicio(models.Model):
    lema = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.lema)


class Entrenar(models.Model):
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()

    class Meta:
        verbose_name = 'Entrenar'
        verbose_name_plural = 'Entrenar'

    def __str__(self):
        return u'{0}'.format(self.lema)


class Nutricion(models.Model):
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()
    contenido3 = models.TextField()

    class Meta:
        verbose_name = 'Nutricion'
        verbose_name_plural = 'Nutricion'

    def __str__(self):
        return u'{0}'.format(self.lema)


class Convenio(models.Model):
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()
    contenido3 = models.TextField()
    corporativos = models.TextField()
    empresariales = models.TextField()

    def __str__(self):
        return u'{0}'.format(self.lema)
