from django.urls import path

from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet

router = SimpleRouter()
router.register('', PaymentViewSet)

app_name = UsersConfig.name

urlpatterns = [

] + router.urls
