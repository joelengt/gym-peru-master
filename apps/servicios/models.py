from django.db import models


class Servicio(models.Model):
    lema = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.ImageField(upload_to='servicio')

    def __str__(self):
        return u'{0}'.format(self.lema)


class Entrenar(models.Model):
    titulo=models.CharField(max_length=20,default="Entrenar")
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()
    imagen = models.ImageField(upload_to='entrenar')

    class Meta:
        verbose_name = 'Entrenar'
        verbose_name_plural = 'Entrenar'

    def __str__(self):
        return u'{0}'.format(self.lema)


class Nutricion(models.Model):
    titulo=models.CharField(max_length=20,default="Nutricion")
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()
    contenido3 = models.TextField()
    imagen = models.ImageField(upload_to='nutricion')

    class Meta:
        verbose_name = 'Nutricion'
        verbose_name_plural = 'Nutricion'

    def __str__(self):
        return u'{0}'.format(self.lema)


class Convenio(models.Model):
    titulo=models.CharField(max_length=20,default="Convenio")
    lema = models.CharField(max_length=250)
    contenido1 = models.TextField()
    contenido2 = models.TextField()
    contenido3 = models.TextField()
    corporativos = models.TextField()
    empresariales = models.TextField()
    imagen = models.ImageField(upload_to='convenio')

    def __str__(self):
        return u'{0}'.format(self.lema)
