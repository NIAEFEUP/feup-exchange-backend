from rest_framework import serializers

from .models import Deadline

class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deadline
        fields = ['time']