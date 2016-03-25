from django.core.mail import send_mail

__author__ = 'klaatu'
from .models import Ruleta, Blog, Video, Imagenes
from rest_framework import serializers


class RuletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruleta


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'created_at', 'fecha', 'titulo', 'categoria', 'imagen_frase', 'slug')


class RetrieveBlogSerializer(serializers.ModelSerializer):
    video = serializers.StringRelatedField(many=True)
    imagenes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog


class ContactanosSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True, max_length=30)
    apellido = serializers.CharField(required=True, max_length=30)
    email = serializers.EmailField(required=True)
    dni = serializers.CharField(required=True)
    celular = serializers.CharField(required=True)
    afiliado = serializers.BooleanField(required=True)
    sexo = serializers.CharField(required=True)
    asunto = serializers.CharField(required=True)
    mensaje = serializers.CharField(required=True)

    def send_mail(self):
        send_mail('Contacto',
                  ''''
                        Nombre: {} {}
                        Email: {}
                        DNI: {}
                        Celular: {}
                        afiliado: {}
                        Sexo: {}
                        asunto:{}
                        Mensaje:
                        {}'''.format(self.validated_data.get('nombre'), self.validated_data.get('apellido'),
                                     self.validated_data.get('email'), self.validated_data.get('dni'),
                                     self.validated_data.get('celular'), self.validated_data.get('afiliado'),
                                     self.validated_data.get('sexo'), self.validated_data.get('asunto'),
                                     self.validated_data.get('mensaje')),
                  self.validated_data.get('email'), ['misterfitnessgym@gmail.com'], fail_silently=False)


class InvitaSerializer(serializers.Serializer):
    nombre1 = serializers.CharField(required=True, max_length=30)
    apellido1 = serializers.CharField(required=True, max_length=30)
    email = serializers.EmailField(required=True)
    dni1 = serializers.CharField(required=True)
    celular = serializers.CharField(required=True)
    sexo1 = serializers.CharField(required=True)
    invitar = serializers.BooleanField(required=True)
    nombre2 = serializers.CharField(required=True, max_length=30)
    apellido2 = serializers.CharField(required=True, max_length=30)
    dni2 = serializers.CharField(required=True)
    sexo2 = serializers.CharField(required=True)

    def send_mail(self):
        send_mail('Contacto',
                  ''''
                        Nombre1: {} {}
                        Email: {}
                        DNI1: {}
                        Celular: {}
                        Sexo1: {}
                        Nombre2: {} {}
                        DNI2: {}
                        Sexo2: {}
                        '''.format(self.validated_data.get('nombre1'), self.validated_data.get('apellido1'),
                                   self.validated_data.get('email'), self.validated_data.get('dni1'),
                                   self.validated_data.get('celular'), self.validated_data.get('sexo1'),
                                   self.validated_data.get('nombre2'), self.validated_data.get('apellido2'),
                                   self.validated_data.get('dni2'), self.validated_data.get('sexo1'),
                                   self.validated_data.get('mensaje')),
                  self.validated_data.get('email'), ['misterfitnessgym@gmail.com'], fail_silently=False)
