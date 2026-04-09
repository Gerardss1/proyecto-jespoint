from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DireccionViewSet

router = DefaultRouter()
router.register(r'direcciones', DireccionViewSet)

urlpatterns = [
    path('', views.login_view),
    path('home', views.home, name='admin_home'),
    path('empleados/', views.empleados_view, name='empleados'),
    # APIs
    path('api/empleados/', views.empleados_api),
    path('api/ubicaciones/', views.ubicaciones_api),
    path('api/empleado/crear/', views.crear_empleado),
    path('api/empleado/<int:id>/editar/', views.editar_empleado),
    path('api/empleado/<int:id>/eliminar/', views.eliminar_empleado),
    path('api/', include(router.urls)),
]
