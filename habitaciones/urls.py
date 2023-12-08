from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'habitacion',views.HabitacionViewSet)

urlpatterns=[
    path('',views.inicio,name="inicio"),
    #path('habitaciones/',include('habitaciones.urls')),
    path('ir_hab',views.ir_hab,name="ir_hab"),
    path('crear',views.crear,name="crear"),
    path('eliminar/<int:codigo>',views.eliminar,name="eliminar"),
    path('editar/<int:codigo>',views.editar,name="editar"),
    path("",include(router.urls)),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)