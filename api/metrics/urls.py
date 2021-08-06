from django.urls import path

from .views import MetricsView

urlpatterns = [
    path("metrics", MetricsView.as_view(), name="info"),
]
