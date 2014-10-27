from django.contrib import admin
from django.conf.urls import url, include
from profiles.models import Profile, ProfileSerializer
from rest_framework import routers, serializers, viewsets

# ViewSets define the view behavior.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profiles/', include('profiles.urls', namespace="profiles")),
    url(r'^admin/', include(admin.site.urls)),
]