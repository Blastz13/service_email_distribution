from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import EmailSubscriberSerializers

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import EmailSubscriber, PageThankYou


class Subscribe(CreateAPIView):
    serializer_class = EmailSubscriberSerializers


class ListSubscribe(ListAPIView):
    serializer_class = EmailSubscriberSerializers
    queryset = EmailSubscriber.objects.all()


class ThankYou(View):
    def get(self, request, slug):
        obj = get_object_or_404(PageThankYou, slug=slug)
        return HttpResponse(open(obj.html_page.path, 'r'))
