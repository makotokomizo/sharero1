from django.urls import path

from . import views

app_name = 'payments'


urlpatterns = [
    path('charge/<token>/', views.charge, name='charge'),
    path('charge/', views.TestView.as_view(), name='charge_kari'),
    path('', views.HomePageView.as_view(), name='home'),
    # path('<int:pk>', views.check, name='cheak'),
    path('<token>', views.check, name='cheak'),
    # path('payout/', views.connect, name='connect'),


    # connect登録
    path('agreement/', views.agreement, name='agreement'),
    path('submit/', views.connect_submit, name='connect_submit'),
    # connect登録

    
    path('ip/', views.MyView.as_view(), name='MyView'),    
]