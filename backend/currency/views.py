from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clients.models import Client
from request_history.models import Request
from .models import Currency
from .serializers import CurrencySerializer


class LatestCurrencyView(APIView):

    def get(self, request):
        queryset = Currency.objects.latest('date')
        user_id = request.query_params.get('user_id')
        client = Client.objects.get(user_id=user_id)
        request_obj = Request(user_id=client, currency=queryset)
        request_obj.save()
        serializer = CurrencySerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
