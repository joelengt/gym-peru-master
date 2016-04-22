#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Clases(models.Model):
    lema = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='clases')

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return u'{0}'.format(self.lema)


class Horas(models.Model):
    hora = models.CharField(max_length=30, help_text='ejemplo de formato en 24 horas (14:00 - 16:00)')

    def __str__(self):
        return u'{0}'.format(self.hora)


class Dia(models.Model):
    nombre = models.CharField(max_length=30)
    dia = models.CharField(max_length=10, choices=(
        ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miércoles'), ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'), ('Sabado', 'Sábado'), ('Domingo', 'Domingo')))
    horas = models.ManyToManyField(Horas, related_name='dhoras')

    def __str__(self):
        return u'{0}-{1}'.format(self.dia, self.nombre)


class Horario(models.Model):
    nombre = models.CharField(max_length=50)
    dias = models.ManyToManyField(Dia, related_name='dias')

    def __str__(self):
        return u'{0}'.format(self.nombre)


class DeportesDeContacto(models.Model):
    titulo=models.CharField(max_length=40,default="Deportes de Contacto")
    tipo = models.CharField(max_length=30, choices=(
        ("PRINCIPAL", "PRINCIPAL"), ("KARATE", "KARATE"), ("BOXEO", "BOXEO"), ("MMA WORKOUT", "MMA WORKOUT"),
        ("KING BOXING", "KING BOXING"), ("MUAY THAI", "MUAY THAI"), ('CAPOEIRA', 'CAPOEIRA')), unique=True)
    descripcion = models.TextField()
    horario = models.ManyToManyField(Horario, related_name='dhorarios', null=True, blank=True)
    imagen = models.ImageField(upload_to='deportes')

    def __str__(self):
        return u'{0}'.format(self.tipo)


class Aerobicos(models.Model):
    titulo=models.CharField(max_length=15,default="Aerobicos")
    tipo = models.CharField(max_length=30, choices=(
        ("PRINCIPAL", "PRINCIPAL"), ('X-BOX', 'X-BOX'), ('FULL BODY', 'FULL BODY'), ('E-FITH', 'E-FITH'),
        ('AERODANCE', 'AERODANCE'), ('BODY-FIT', 'BODY-FIT'), ('BAILE', 'BAILE'), ('LOCALIZADO', 'LOCALIZADO'),
        ('STEP LOCAL', 'STEP LOCAL')),
                            unique=True)
    descripcion = models.TextField()
    horario = models.ManyToManyField(Horario, related_name='ahorarios', null=True, blank=True)
    imagen = models.ImageField(upload_to='aerobicos')

    def __str__(self):
        return u'{0}'.format(self.tipo)


class Talleres(models.Model):
    titulo=models.CharField(max_length=15,default="Talleres")
    tipo = models.CharField(max_length=30, choices=(("PRINCIPAL", "PRINCIPAL"), ('BAILE MODERNO', 'BAILE MODERNO'),
                                                    ('FULL BODY KIDS', 'FULL BODY KIDS'), ('MARINERA', 'MARINERA')),
                            unique=True)
    descripcion = models.TextField()
    horario = models.ManyToManyField(Horario, related_name='thorarios', null=True, blank=True)
    imagen = models.ImageField(upload_to='talleres')

    class Meta:
        verbose_name_plural = 'Talleres'
        verbose_name = 'Taller'

    def __str__(self):
        return u'{0}'.format(self.tipo)


class BestCyclng(models.Model):
    titulo=models.CharField(max_length=20,default="Bestcycling")
    tipo = models.CharField(max_length=30, choices=(("PRINCIPAL", "PRINCIPAL"), ('SPINNING', 'SPINNING'),
                                                    ('BESET CYCLING', 'BEST CYCLING')), unique=True)
    descripcion = models.TextField()
    horario = models.ManyToManyField(Horario, related_name='bhorarios', null=True, blank=True)
    imagen = models.ImageField(upload_to='best')

    def __str__(self):
        return u'{0}'.format(self.tipo)
