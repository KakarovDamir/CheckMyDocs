from dataclasses import fields
from rest_framework import serializers

from api.models import FileData


class FileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = '__all__'