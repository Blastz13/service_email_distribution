from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import EmailSubscriberSerializers

from .models import EmailSubscriber


class Subscribe(CreateAPIView):
    serializer_class = EmailSubscriberSerializers


class ListSubscribe(ListAPIView):
    serializer_class = EmailSubscriberSerializers
    queryset = EmailSubscriber.objects.all()
