from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Request
from .serializers import RequestSerializer


class UserRequestsView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')  # Получаем user_id из query параметров

        # Получаем объекты Request, совпадающие с user_id
        requests = Request.objects.filter(user_id=user_id)[:5]
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

