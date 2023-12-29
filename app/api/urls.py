from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from api.views import TaskViewSet

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    
    path('', include(router.urls)),
]