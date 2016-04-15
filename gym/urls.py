from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from apps.blog.views import IndexView, ServiciosView, ClasesView, BlogView,VisitanosView,ContactanosView,ServiciosInteriorView

urlpatterns = [
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.blog.urls')),
    url(r'^api/', include('apps.clases.urls')),
    url(r'^api/', include('apps.servicios.urls')),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^servicios/$', ServiciosView.as_view(), name='servicios'),
    url(r'^servicios/entrenar/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^servicios/nutricion/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^servicios/convenio/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^clases/$', ClasesView.as_view(), name='clases'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^visitanos/$', VisitanosView.as_view(), name='visitanos'),
    url(r'^contactanos/$', ContactanosView.as_view(), name='contactanos'),

]
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}), )
