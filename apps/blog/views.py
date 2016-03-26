from django.shortcuts import render

# Create your views here.
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
        return Response( status=status.HTTP_200_OK)
