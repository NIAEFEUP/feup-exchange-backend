from django.urls import path

from .views import AdminTestServiceView, AdminView

urlpatterns = [
    path('', AdminView.as_view(), name="user"),
    path('test/', AdminTestServiceView.as_view(), name="admintest"),
]