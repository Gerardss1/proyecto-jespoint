from django.urls import path 
from .views import *
from rest_framework.routers import DefaultRouter
from .views import DireccionViewSet

urlpatterns=[
    path('home/', home, name='admin_home'),

]

router = DefaultRouter()
router.register(r'direcciones', DireccionViewSet)

urlpatterns = router.urls