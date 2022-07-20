from django.urls import path

from .views import DeadlineView

urlpatterns = [
    path('deadline/', DeadlineView.as_view(), name="deadline"),
]