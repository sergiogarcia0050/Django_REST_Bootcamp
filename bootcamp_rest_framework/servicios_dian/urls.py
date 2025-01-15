from django.urls import include, path
from rest_framework import routers

from bootcamp_rest_framework.servicios_dian.views import vistasDian

router = routers.SimpleRouter()

router.register(r'vistasDian', vistasDian)

urlpatterns = [
    path('', include(router.urls))
]
