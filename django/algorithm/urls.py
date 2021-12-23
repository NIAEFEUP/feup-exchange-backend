from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import AlgorithmScheduleView

urlpatterns = [
    path('', AlgorithmScheduleView.as_view(), name="alg_schedule")
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
