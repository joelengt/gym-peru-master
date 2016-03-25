__author__ = 'klaatu'
from rest_framework import serializers
from .models import *


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio


class NutricionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricion


class EntrenarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenar


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
