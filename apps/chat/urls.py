from django.urls import path

from .views import MessageView


urlpatterns = [
    # API views endpoints
    path('messages/', MessageView.as_view(), name='messages'),
]
