from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^clases/$', ClasesAPIView.as_view()),
    url(r'^deportes-de-contacto-principal/$', DeporteDeContactoPAPIView.as_view()),
    url(r'^bestcicling-principal/$', BestCyclingPAPIView.as_view()),
    url(r'^aerobicos-principal/$', AerobicosPAPIView.as_view()),
    url(r'^talleres-principal/$', TalleresPAPIView.as_view()),
    url(r'^deportes-de-contacto/$', DeporteDeContactoAPIView.as_view()),
    url(r'^bestcicling/$', BestCyclingAPIView.as_view()),
    url(r'^aerobicos/$', AerobicosAPIView.as_view()),
    url(r'^talleres/$', TalleresAPIView.as_view()),
    url(r'^deportes-de-contacto/(?P<pk>\d+)/(?P<tipo>[\w-]+)/$', RetrieveDeporteDeContactoAPIView.as_view()),
    url(r'^bestcicling/(?P<pk>\d+)/(?P<tipo>[\w-]+)/$', RetrieveBestCyclingAPIView.as_view()),
    url(r'^aerobicos/(?P<pk>\d+)/(?P<tipo>[\w-]+)/$', RetrieveAerobicosAPIView.as_view()),
    url(r'^talleres/(?P<pk>\d+)/(?P<tipo>[\w-]+)/$', RetrieveTalleresAPIView.as_view()),
]
