from rest_framework import serializers
from owner.models import owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = '__all__'
