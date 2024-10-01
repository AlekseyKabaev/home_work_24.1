from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payment_method', 'payed_course', 'payed_lesson')
    ordering_fields = ('pay_date',)
    ordering = ('pay_date',)
