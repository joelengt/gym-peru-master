__author__ = 'klaatu'
from rest_framework import serializers
from .models import *


class ClasesSerializer(serializers.ModelSerializer):
    bestcycling_descripcion = serializers.SerializerMethodField()
    bestcycling_imagen = serializers.SerializerMethodField()
    deportes_descripcion = serializers.SerializerMethodField()
    deportes_imagen = serializers.SerializerMethodField()
    aerobicos_descripcion = serializers.SerializerMethodField()
    aerobicos_imagen = serializers.SerializerMethodField()
    talleres_descripcion = serializers.SerializerMethodField()
    talleres_imagen = serializers.SerializerMethodField()

    class Meta:
        model = Clases
        fields = (
            'lema', 'imagen', 'bestcycling_descripcion', 'bestcycling_imagen', 'deportes_descripcion',
            'deportes_imagen', 'aerobicos_descripcion', 'aerobicos_imagen', 'talleres_descripcion', 'talleres_imagen')

    def get_bestcycling_descripcion(self, obj):
        descripcion = BestCyclng.objects.get(tipo='PRINCIPAL').descripcion
        return descripcion

    def get_deportes_descripcion(self, obj):
        descripcion = DeportesDeContacto.objects.get(tipo='PRINCIPAL').descripcion
        return descripcion

    def get_aerobicos_descripcion(self, obj):
        descripcion = Aerobicos.objects.get(tipo='PRINCIPAL').descripcion
        return descripcion

    def get_talleres_descripcion(self, obj):
        descripcion = Talleres.objects.get(tipo='PRINCIPAL').descripcion
        return descripcion

    def get_bestcycling_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = BestCyclng.objects.get(id=1).imagen.url
        b_imagen = request.build_absolute_uri(imagen_url)
        return b_imagen

    def get_deportes_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = DeportesDeContacto.objects.get(id=1).imagen.url
        d_imagen = request.build_absolute_uri(imagen_url)
        return d_imagen

    def get_aerobicos_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = Aerobicos.objects.get(id=1).imagen.url
        a_imagen = request.build_absolute_uri(imagen_url)
        return a_imagen

    def get_talleres_imagen(self, obj):
        request = self.context.get('request')
        imagen_url = Talleres.objects.get(id=1).imagen.url
        t_imagen = request.build_absolute_uri(imagen_url)
        return t_imagen


class DiasSerializer(serializers.ModelSerializer):
    horas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Dia
        fields = ('dia', 'horas')


class HorarioSerializer(serializers.ModelSerializer):
    dias = DiasSerializer(many=True, read_only=True)

    class Meta:
        model = Horario


class DeporteDeContactoSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = DeportesDeContacto


class BestCyclingSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = BestCyclng


class AerobicosSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = Aerobicos


class TalleresSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = Talleres
