from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from measurements import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'measurements', views.MeasurementViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
