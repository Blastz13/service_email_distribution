from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmailSubscriberSerializers

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import EmailSubscriber, PageThankYou


class Subscribe(APIView):
    def post(self, request):
        serializer = EmailSubscriberSerializers(data=request.data)
        if serializer.is_valid():
            try:
                obj = EmailSubscriber.objects.get(phone=serializer.validated_data['phone'])
                obj.email = serializer.validated_data['email']
                obj.save()
            except:
                serializer.save()
        return Response(status=201)


class ListSubscribe(ListAPIView):
    serializer_class = EmailSubscriberSerializers
    queryset = EmailSubscriber.objects.all()


class ThankYou(View):
    def get(self, request, slug):
        obj = get_object_or_404(PageThankYou, slug=slug)
        return HttpResponse(open(obj.html_page.path, 'r'))
