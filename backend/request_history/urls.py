from django.urls import path
from request_history.apps import RequestHistoryConfig
from request_history.views import UserRequestsView

app_name = RequestHistoryConfig.name

urlpatterns = [
    path('history/', UserRequestsView.as_view(), name='history'),
]
