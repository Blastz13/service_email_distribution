from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import Subscribe, ListSubscribe, ThankYou


urlpatterns = [
    path('subscribe/', Subscribe.as_view()),
    path('list-subscribe/', ListSubscribe.as_view()),
    path('thank-you/', ThankYou.as_view()),
]
