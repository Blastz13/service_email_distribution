from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import EmailSubscriberSerializers

from django.shortcuts import render
from django.views import View

from .models import EmailSubscriber


class Subscribe(CreateAPIView):
    serializer_class = EmailSubscriberSerializers


class ListSubscribe(ListAPIView):
    serializer_class = EmailSubscriberSerializers
    queryset = EmailSubscriber.objects.all()


class ThankYou(View):
    def get(self, request):
        return render(request, 'email_distribution/confirm.html')
