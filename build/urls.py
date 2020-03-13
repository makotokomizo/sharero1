from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

app_name = 'build'

# print("here.urls")

urlpatterns = [
    # path('chattest/', views.chatTest, name='chatTest'),
    # re_path('.*', TemplateView.as_view(template_name='./index.html')),
    # path('', TemplateView.as_view(template_name='./index.html')),
    path('', views.index),
]
