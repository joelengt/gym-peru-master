from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^servicios/$', ServiciosAPIView.as_view()),
    url(r'^nutricion/$', NutricionAPIView.as_view()),
    url(r'^convenio/$', ConvenioAPIView.as_view()),
    url(r'^entrenar/$', EntrenarAPIView.as_view()),
]
