from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from rest_framework import generics, filters, status
from rest_framework.response import Response
from apps.blog.serializers import ContactanosSerializer, InvitaSerializer
from .models import Blog, Ruleta
from .serializers import HomeSerializer, RuletaSerializer, RetrieveBlogSerializer


class HomeAPIView(generics.ListAPIView):
    serializer_class = HomeSerializer
    queryset = Blog.objects.all()[:12]


class SearchBlogAPIView(generics.ListAPIView):
    serializer_class = HomeSerializer
    queryset = Blog.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('categoria',)


class RetrieveBlogAPIView(generics.RetrieveAPIView):
    serializer_class = RetrieveBlogSerializer
    queryset = Blog.objects.all()


class RuletaAPIView(generics.ListAPIView):
    serializer_class = RuletaSerializer
    queryset = Ruleta.objects.all()


class ContactanosAPIView(generics.GenericAPIView):
    serializer_class = ContactanosSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_mail()
        return Response(status=status.HTTP_200_OK)


class InvitaAPIView(generics.GenericAPIView):
    serializer_class = InvitaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_mail()
        return Response(status=status.HTTP_200_OK)


class IndexView(TemplateView):
    template_name = 'index.html'


class ServiciosView(TemplateView):
    template_name = 'servicios.html'


class ServiciosInteriorView(TemplateView):
    template_name = 'serviciointerior.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class ClasesView(TemplateView):
    template_name = 'clases.html'

class ClasesInteriorView(TemplateView):
    template_name = 'clasesinterior.html'

class ContactanosView(TemplateView):
    template_name = 'contacto.html'

class VisitanosView(TemplateView):
    template_name = 'visitanos.html'

class ClasesInterior2View(TemplateView):
    template_name = 'clasesinterior2.html'

class BlogInteriorView(TemplateView):
    template_name = 'bloginterior.html'
