from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers import APITokenObtainPairSerializer


class APITokenObtainPairView(TokenObtainPairView):
    serializer_class = APITokenObtainPairSerializer
