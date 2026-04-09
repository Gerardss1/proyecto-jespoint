
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_geoger.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include('admin_geoger.urls')),
    
    
]
