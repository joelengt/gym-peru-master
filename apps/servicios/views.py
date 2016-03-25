from .serializers import *
from .models import *
from rest_framework import generics


class ServiciosAPIView(generics.ListAPIView):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()[:1]


class NutricionAPIView(generics.ListAPIView):
    serializer_class = NutricionSerializer
    queryset = Nutricion.objects.all()[:1]


class ConvenioAPIView(generics.ListAPIView):
    serializer_class = ConvenioSerializer
    queryset = Convenio.objects.all()[:1]


class EntrenarAPIView(generics.ListAPIView):
    serializer_class = EntrenarSerializer
    queryset = Entrenar.objects.all()[:1]
