from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Currency API",
      default_version='v1',
      description="Documentation for currency market storage",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="roman.ecm@mail.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls', namespace='users')),
    path('api/v1/', include('clients.urls', namespace='clients')),
    path('api/v1/', include('currency.urls', namespace='currency')),
    path('api/v1/', include('request_history.urls', namespace='history')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]