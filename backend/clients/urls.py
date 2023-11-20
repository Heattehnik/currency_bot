from django.urls import path
from clients.apps import ClientsConfig
from clients.views import ClientCreateView, ChangeSubscriptionStatus

app_name = ClientsConfig.name

urlpatterns = [
    path('client/', ClientCreateView.as_view(), name='create_client'),
    path('subscribe/<int:user_id>/', ChangeSubscriptionStatus.as_view(), name="subscription")
]
