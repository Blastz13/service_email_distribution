from django.urls import path

from .views import Subscribe, ListSubscribe, ThankYou


urlpatterns = [
    path('subscribe/', Subscribe.as_view()),
    path('list-subscribe/', ListSubscribe.as_view()),
    path('<slug:slug>/thank-you/', ThankYou.as_view()),
]
