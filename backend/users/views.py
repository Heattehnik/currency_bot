from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class TokenObtain(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data["password"])
        user.save()
        return user
