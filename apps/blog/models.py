from django.db import models
from tinymce.models import HTMLField


class Ruleta(models.Model):
    imagen1 = models.ImageField(upload_to='Ruleta')
    imagen2 = models.ImageField(upload_to='Ruleta')
    imagen3 = models.ImageField(upload_to='Ruleta')
    imagen4 = models.ImageField(upload_to='Ruleta')

    class Meta:
        verbose_name_plural = 'Ruletas'
        verbose_name = 'Ruleta'


class Video(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Imagenes(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='imagenes')

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(help_text='No llenar, este campo se llena solo')
    frase = models.CharField(max_length=250)
    imagen_frase = models.ImageField(upload_to='fraseimagen')
    fecha = models.DateField(auto_now=True)
    categoria = models.CharField(max_length=40, choices=(
        ('Actualidad', 'Actualidad'), ('Fitnes', 'Fitnes'), ('Nutricion', 'Nutrición')))
    contenido = HTMLField()
    video = models.ManyToManyField(Video, related_name='videos', blank=True, null=True)
    facebook = models.URLField(null=True, blank=True)
    mas_info = models.URLField(null=True, blank=True)
    imagenes = models.ManyToManyField(Imagenes, related_name='imagenes',null=True,blank=True)
    instagram = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return u'{0}--{1}'.format(self.titulo, self.slug)
