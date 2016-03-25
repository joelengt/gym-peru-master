__author__ = 'klaatu'
from rest_framework import serializers
from .models import *


class ClasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clases


class DiasSerializer(serializers.ModelSerializer):
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
