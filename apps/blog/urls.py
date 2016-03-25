from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^home/$', HomeAPIView.as_view()),
    url(r'^ruleta/$', RuletaAPIView.as_view()),
    url(r'^blog/$', SearchBlogAPIView.as_view()),
    url(r'^blog/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', RetrieveBlogAPIView.as_view()),
    url(r'^invita/$', InvitaAPIView.as_view()),
    url(r'^contactanos/$', ContactanosAPIView.as_view()),
]