from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dialog_flow.views import webhookDialog

urlpatterns = [
    path('webhook/', webhookDialog.as_view(), name='webhook')
]