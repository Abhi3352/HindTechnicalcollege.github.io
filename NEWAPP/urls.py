from django.urls import path
from . import views
urlpatterns = [
    #################### Paths Paths for Html File #######################
    path('boot', views.boot, name='boot'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='home'),  
    path('cont', views.cont, name='cont'), 
    path('about', views.about, name='about'),
    path('application', views.application, name='application'),
    path('appliform', views.appliform, name='appliform'),

]