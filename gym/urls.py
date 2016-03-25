from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
    #url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.blog.urls')),
    url(r'^api/', include('apps.clases.urls')),
    url(r'^api/', include('apps.servicios.urls')),

]
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}),)