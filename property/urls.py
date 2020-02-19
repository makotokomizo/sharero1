from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:id>', views.property_detail, name='property_detail'),
    path('submit1/', views.property_submit1, name='property_submit1'),
    path('submit2/', views.property_submit2, name='property_submit2'),
    path('submit3/', views.property_submit3, name='property_submit3'),
    path('submit4/', views.property_submit4, name='property_submit4'),
    path('submit5/', views.property_submit5, name='property_submit5'),
    path('end/', views.property_end, name='property_end'),
    path('submit/complete/', views.property_submit_complete, name='property_submit_complete'),
    path('detail/<int:pk>/', views.property_my_detail, name='property_my_detail'),
    # path(r'^(?P<pk>\d+)/detail$', views.property_my_detail, name='property_my_detail'),
    path('edit/<int:pk>/', views.property_edit, name='property_edit'),
    # path('edit/<int:pk>/', views.property_edit.as_view(), name='property_edit'),

    path('property_data', views.property_list, name='property_list'),
    # path('property_data_input/', views.user_data_input, name='user_data_input'),
    # path('property_data_confirm/', views.user_data_confirm, name='user_data_confirm'),
    # path('property_data_create/', views.user_data_create, name='user_data_create'),
]