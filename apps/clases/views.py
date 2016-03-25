from .serializers import *
from .models import *
from rest_framework import generics


class ClasesAPIView(generics.ListAPIView):
    serializer_class = ClasesSerializer
    queryset = Clases.objects.all()


class DeporteDeContactoPAPIView(generics.ListAPIView):
    serializer_class = DeporteDeContactoSerializer
    queryset = DeportesDeContacto.objects.filter(tipo='PRINCIPAL')


class BestCyclingPAPIView(generics.ListAPIView):
    serializer_class = BestCyclingSerializer
    queryset = BestCyclng.objects.filter(tipo='PRINCIPAL')


class AerobicosPAPIView(generics.ListAPIView):
    serializer_class = AerobicosSerializer
    queryset = Aerobicos.objects.filter(tipo='PRINCIPAL')


class TalleresPAPIView(generics.ListAPIView):
    serializer_class = TalleresSerializer
    queryset = Talleres.objects.filter(tipo='PRINCIPAL')


class DeporteDeContactoAPIView(generics.ListAPIView):
    serializer_class = DeporteDeContactoSerializer
    queryset = DeportesDeContacto.objects.all()


class BestCyclingAPIView(generics.ListAPIView):
    serializer_class = BestCyclingSerializer
    queryset = BestCyclng.objects.all()


class AerobicosAPIView(generics.ListAPIView):
    serializer_class = AerobicosSerializer
    queryset = Aerobicos.objects.all()


class TalleresAPIView(generics.ListAPIView):
    serializer_class = TalleresSerializer
    queryset = Talleres.objects.all()


class RetrieveDeporteDeContactoAPIView(generics.RetrieveAPIView):
    serializer_class = DeporteDeContactoSerializer
    queryset = DeportesDeContacto.objects.all()


class RetrieveBestCyclingAPIView(generics.RetrieveAPIView):
    serializer_class = BestCyclingSerializer
    queryset = BestCyclng.objects.all()


class RetrieveAerobicosAPIView(generics.RetrieveAPIView):
    serializer_class = AerobicosSerializer
    queryset = Aerobicos.objects.all()


class RetrieveTalleresAPIView(generics.RetrieveAPIView):
    serializer_class = TalleresSerializer
    queryset = Talleres.objects.all()
