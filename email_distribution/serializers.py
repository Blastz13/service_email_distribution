from rest_framework import serializers

from .models import EmailSubscriber


class EmailSubscriberSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmailSubscriber
        fields = ('name', 'phone', 'email', 'geo')
