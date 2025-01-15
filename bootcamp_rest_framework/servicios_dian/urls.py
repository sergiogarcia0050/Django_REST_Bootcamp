# from django.urls import include, path
# from rest_framework import routers

# from servicios_dian.views import vistasDian

# router = routers.SimpleRouter()
# router.register(r'vistasDian', vistasDian)

from django.urls import path
from .views import ExternalServiceView

urlpatterns = [
    path('external-data/', ExternalServiceView.as_view(), name='external-data'),
]