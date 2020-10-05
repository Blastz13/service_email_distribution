from django.urls import path

from .views import Subscribe, ListSubscribe


urlpatterns = [
    path('subscribe/', Subscribe.as_view()),
    path('list-subscribe/', ListSubscribe.as_view()),
]
