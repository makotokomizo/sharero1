from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('property/', include('property.urls', namespace='property')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('register/', include('register.urls', namespace='register')),
    

    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('payments/', include('payments.urls')),
    
    # path('chat/', include('chat.urls', namespace='chat')),
    # path('public/', include('public.urls', namespace='public')),
    # path('build/', include('build.urls', namespace='build')),
    # path('build-test/', include('build-test.urls', namespace='build-test')),
    # path('react/', TemplateView.as_view(template_name='index-react.html')),
    # path('talk/', TemplateView.as_view(template_name='index.html')),
    # re_path('.*', TemplateView.as_view(template_name='index.html')),
    # path('front/', TemplateView.as_view(template_name='index.html')),
    # path('api/', include('todos.api.urls', namespace='todos')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ShareRo RESERVATION ADMIN'
admin.site.site_title = 'ShareRo RESERVATION ADMIN'
admin.site.site_index_title = 'Welcome to ShareRo Reservation Admin'