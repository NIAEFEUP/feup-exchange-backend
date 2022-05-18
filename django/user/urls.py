from django.urls import path

from .views import AdminTestServiceView

urlpatterns = [
    path('', AdminTestServiceView.as_view(), name="admintest")
]