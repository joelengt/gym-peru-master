__author__ = 'klaatu'
from rest_framework import serializers
from .models import *


class ServicioSerializer(serializers.ModelSerializer):
    nutricion_lema = serializers.SerializerMethodField()
    nutricion_imagen = serializers.SerializerMethodField()
    convenio_lema = serializers.SerializerMethodField()
    convenio_imagen = serializers.SerializerMethodField()
    entrenar_lema = serializers.SerializerMethodField()
    entrenar_imagen = serializers.SerializerMethodField()

    class Meta:
        model = Servicio
        fields = (
        'id', 'lema', 'nutricion_lema', 'nutricion_imagen', 'convenio_lema', 'convenio_imagen', 'entrenar_lema',
        'entrenar_imagen')

    def get_nutricion_lema(self, obj):
        lema = Nutricion.objects.get(id=1).lema
        return lema

    def get_convenio_lema(self, obj):
        lema = Convenio.objects.get(id=1).lema
        return lema

    def get_entrenar_lema(self, obj):
        lema = Entrenar.objects.get(id=1).lema
        return lema

    def get_nutricion_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = Nutricion.objects.get(id=1).imagen.url
        n_imagen = request.build_absolute_uri(imagen_url)
        return n_imagen

    def get_convenio_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = Convenio.objects.get(id=1).imagen.url
        c_imagen = request.build_absolute_uri(imagen_url)
        return c_imagen

    def get_entrenar_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = Entrenar.objects.get(id=1).imagen.url
        e_imagen = request.build_absolute_uri(imagen_url)
        return e_imagen


class NutricionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricion


class EntrenarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenar


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
