from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('subscribe/', subscribe, name='subscribe'),
    
    # service
    path('service/<int:id>/', service, name='service'),

    path('contact/', contact, name="contact"),

    # login
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    # dashboard
    path('dashboard/', dashboard, name='dashboard'),
]