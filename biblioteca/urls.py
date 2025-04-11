from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuprincipal_wiki, name="menuprincipal_wiki"),
    path('armas/', views.armas, name='armas'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('flora/', views.flora, name='flora'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('lugares/', views.lugarestf, name='lugarestf'),
    path('logros/', views.logros, name='logros'),
    path('animales/', views.animales, name='animales'),
    path('historia/', views.historia, name='historia'),
    path('foro/', views.forowiki, name='forowiki'),
    
    # URLs de autenticacion
    path('login/', views.inicio_sesion_wiki, name='inicio_sesion_wiki'),
    path('registro/', views.registrase_wiki, name='registrase_wiki'),
    path('recuperar-contrasena/', views.recuperarcontra, name='recuperarcontra'),
    path('mi-cuenta/', views.micuentatf, name='micuentatf'),
]