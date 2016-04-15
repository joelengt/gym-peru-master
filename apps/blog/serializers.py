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
    nombre = serializers.CharField(required=True, max_length=30)
    apellido = serializers.CharField(required=True, max_length=30)
    email = serializers.EmailField(required=True)
    dni = serializers.CharField(required=True,)
    celular = serializers.CharField(required=True)
    sexo = serializers.CharField(required=True)
    invitar = serializers.BooleanField(required=False)
    nombre_invitado = serializers.CharField(required=False,max_length=30)
    apellido_invitado = serializers.CharField(required=False,max_length=30)
    dni_invitado = serializers.CharField(required=False)
    sexo_invitado = serializers.CharField(required=False)

    def send_mail(self):
        if self.validated_data.get('invitar')==True:
            send_mail('Contacto',
                      ''''
                            Nombre: {} {}
                            Email: {}
                            DNI: {}
                            Celular: {}
                            Sexo: {}
                            Nombre Invitado: {} {}
                            DNI Invitado: {}
                            Sexo Invitado: {}
                            '''.format(self.validated_data.get('nombre'), self.validated_data.get('apellido'),
                                       self.validated_data.get('email'), self.validated_data.get('dni'),
                                       self.validated_data.get('celular'), self.validated_data.get('sexo'),
                                       self.validated_data.get('nombre_invitado'), self.validated_data.get('apellido_invitado'),
                                       self.validated_data.get('dni_invitado'), self.validated_data.get('sexo_invitado')),
                      self.validated_data.get('email'), ['misterfitnessgym@gmail.com'], fail_silently=False)
        else:
            send_mail('Contacto',
                      ''''
                            Nombre: {} {}
                            Email: {}
                            DNI: {}
                            Celular: {}
                            Sexo: {}
                            '''.format(self.validated_data.get('nombre'), self.validated_data.get('apellido'),
                                       self.validated_data.get('email'), self.validated_data.get('dni'),
                                       self.validated_data.get('celular'), self.validated_data.get('sexo')),
                      self.validated_data.get('email'), ['misterfitnessgym@gmail.com'], fail_silently=False)
