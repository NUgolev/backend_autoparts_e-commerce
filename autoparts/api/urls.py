from rest_framework.routers import DefaultRouter

from .views import view_sets

router = DefaultRouter()

for route, view in view_sets:
    router.register(route, view)

urlpatterns = router.urls
