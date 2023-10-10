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
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    # update
    path('update/', update, name='update'),


    # dashboard
    path('dashboard/', dashboard, name='dashboard'),
    
    # order
    path('order/<int:id>/', order, name='order'),
]